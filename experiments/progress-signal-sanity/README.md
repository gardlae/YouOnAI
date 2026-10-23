# Progress signal sanity exercise

This small, dependency-free Python exercise illustrates the proposed signal definitions. It is **not a robot simulator, RL training run, learned model, or research result**. Values and completion labels are hand-authored to demonstrate a setback and an incorrect completion declaration.

From the repository root:

```bash
python3 experiments/progress-signal-sanity/signals.py
python3 -m unittest discover -s experiments/progress-signal-sanity -p 'test_*.py'
```

The first command prints CSV with progress, cost, signed progress change, discounted shaping reward, a proposed completion decision, and independent toy truth. The transition from `lift` to `drop` has falling progress and rising cost. `looks_seated` deliberately has a false completion declaration. Compare it with `verified_seated`.

Questions: Why can discounted shaping be negative even with no regression? Why does progress 0.95 not prove completion? Why is no declaration an undefined false-declaration fraction rather than zero error? Why must true terminal transitions and time-limit truncations be handled differently?

The helper implements one transition's potential term, not subgoal switching, a POMDP model, temporal verification or a complete trainer. `terminated=True` imposes zero absorbing-terminal potential; pass `False` for a time-limit truncation when the underlying process continues. The terminal demonstration sets a unit base success reward solely for teaching. Real experiments must specify their objective and scale; do not copy the synthetic values as a reward design.

See the [research method](../../research/projects/verified-subgoal-rl/method.md) for the proposed interfaces and limitations.
