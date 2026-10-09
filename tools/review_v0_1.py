"""Review the original v0.1 fixtures; this is not a conformance engine.

Run with Python 3.11+ and jsonschema[format]==4.26.0 installed.
Checks baseline arithmetic and selected structural/semantic relationships only.
It deliberately does not resolve the proposed policies in RFC 0002.
"""
import json, copy, statistics
from pathlib import Path
from datetime import datetime
from jsonschema import Draft202012Validator, FormatChecker
root = Path(__file__).resolve().parents[1]

def read(p):
    return json.loads((root / p).read_text())

def ts(x):
    return datetime.fromisoformat(x.replace('Z', '+00:00'))
validators = {}
for kind in ['service', 'change', 'deployment', 'incident', 'event-envelope']:
    s = read(f'schemas/v0.1/{kind}.schema.json')
    Draft202012Validator.check_schema(s)
    validators[kind] = Draft202012Validator(s, format_checker=FormatChecker())
count = 0
examples = read('examples/v0.1/records.json')
for kind, r in examples.items():
    validators['event-envelope' if kind == 'envelope' else kind].validate(r)
    count += 1
validators[examples['envelope']['record_type']].validate(examples['envelope']['payload'])
count += 1
for p in sorted((root / 'conformance/v0.1/cases').glob('*.json')):
    d = json.loads(p.read_text())
    e = read('conformance/v0.1/expected-results/' + p.name)
    for plural, kind in [('services', 'service'), ('changes', 'change'), ('deployments', 'deployment'), ('incidents', 'incident')]:
        for r in d[plural]:
            validators[kind].validate(r)
            count += 1
        assert len({r['id'] for r in d[plural]}) == len(d[plural])
    services = {r['id'] for r in d['services']}
    changes = {r['id']: r for r in d['changes']}
    deps = {r['id']: r for r in d['deployments']}
    for r in deps.values():
        assert r['service_id'] in services
        assert all((c in changes for c in r['change_ids']))
        if r['qualification'] == 'qualifying':
            assert r['environment'] == 'production' and r['effective_at'] is not None
    for r in d['incidents']:
        assert r['service_id'] in services and r['causal_deployment_id'] in deps
        assert deps[r['causal_deployment_id']]['service_id'] == r['service_id']
        assert not r['restored_at'] or ts(r['restored_at']) >= ts(r['failure_started_at'])
    start, end = (ts(d['window']['start']), ts(d['window']['end']))
    population = [r for r in deps.values() if r['service_id'] == e['service_id'] and r['qualification'] == 'qualifying' and (start <= ts(r['effective_at']) < end)]
    n = len(population)
    assert e['deployment_frequency']['count'] == n
    assert e['deployment_frequency']['deployments_per_day'] == n / d['window']['calendar_days']
    durations = []
    for c in changes.values():
        times = [ts(r['effective_at']) for r in deps.values() if r['service_id'] == e['service_id'] and r['qualification'] == 'qualifying' and (c['id'] in r['change_ids'])]
        if times and start <= min(times) < end:
            seconds = (min(times) - ts(c['committed_at'])).total_seconds()
            assert seconds >= 0
            durations.append(seconds)
    assert e['change_lead_time']['observation_count'] == len(durations)
    assert e['change_lead_time']['median_seconds'] == (statistics.median(durations) if durations else None)
    for metric, field, value in [('change_fail_rate', 'failure', 'failed'), ('deployment_rework_rate', 'rework', 'incident_driven')]:
        numerator = sum((r[field] == value for r in population))
        unknown = sum((r[field] == 'unknown' for r in population))
        expected = {'numerator': numerator, 'denominator': n, 'unknown_count': unknown, 'lower_bound': numerator / n if n else None, 'upper_bound': (numerator + unknown) / n if n else None, 'status': 'no_observations' if not n else 'provisional' if unknown else 'complete'}
        assert expected == e[metric]
    episodes = [r for r in d['incidents'] if r['service_id'] == e['service_id'] and start <= ts(r['failure_started_at']) < end]
    recovery = [(ts(r['restored_at']) - ts(r['failure_started_at'])).total_seconds() for r in episodes if r['restored_at']]
    assert e['failed_deployment_recovery_time']['median_seconds'] == (statistics.median(recovery) if recovery else None)
    assert e['failed_deployment_recovery_time']['observation_count'] == len(recovery)
    assert e['failed_deployment_recovery_time']['open_count'] == sum((r['restored_at'] is None for r in episodes))
    print(p.stem + ': record shapes, baseline references/order and all numeric metric fields match')
print(f'{len(validators)} schemas checked; {count} record/payload validations passed')
base = read('conformance/v0.1/cases/complete.json')
assert sum((not r['change_ids'] for r in base['deployments'])) == 9
print('complete: 9/10 deployments have empty change_ids, yet lead time status is complete')
probes = {}
r = copy.deepcopy(base['incidents'][0])
r['restored_at'] = '2026-10-13T08:35:00Z'
probes['restoration after evidence cutoff'] = ('incident', r)
r = copy.deepcopy(base['incidents'][0])
r['service_id'] = 'service:other'
probes['incident service differs from causal deployment'] = ('incident', r)
r = copy.deepcopy(base['incidents'][0])
r['failure_started_at'] = '2026-10-04T08:05:00Z'
r['restored_at'] = '2026-10-04T08:35:00Z'
probes['failure onset precedes causal deployment'] = ('incident', r)
r = copy.deepcopy(base['deployments'][0])
r['qualification'] = 'unknown'
r['effective_at'] = None
probes['unknown qualification with no time for window membership'] = ('deployment', r)
for name, (kind, r) in probes.items():
    validators[kind].validate(r)
    print('shape-valid counterexample: ' + name)
print('These probes demonstrate missing semantic policy, not a promise that schema validation handles cross-record rules.')
