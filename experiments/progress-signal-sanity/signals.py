"""Illustrative signal arithmetic only; no simulator or learned predictions."""

import csv
import math
import sys


def potential_shaping(previous, current, gamma=0.99, *, terminated=False):
    """Return gamma * Phi(next) - Phi(previous) with terminal Phi(next)=0."""
    if not all(math.isfinite(x) for x in (previous, current, gamma)):
        raise ValueError("Potentials and discount must be finite")
    if not 0 <= gamma <= 1:
        raise ValueError("gamma must be in [0, 1]")
    return gamma * (0.0 if terminated else current) - previous


def completion_summary(declarations, truths):
    """One decision and independent truth per episode; no frame pooling."""
    if len(declarations) != len(truths) or not declarations:
        raise ValueError("Provide equal-length, nonempty episode records")
    if any(type(x) is not bool for x in (*declarations, *truths)):
        raise ValueError("Decisions and truth labels must be booleans")
    declared = sum(declarations)
    false = sum(d and not t for d, t in zip(declarations, truths))
    return {
        "episodes": len(truths),
        "declaration_coverage": declared / len(truths),
        "false_completion_among_declarations": false / declared if declared else None,
        "environment_success_rate": sum(truths) / len(truths),
    }


def main():
    # Hand-authored mathematical example, not logged robot observations.
    events = [
        ("approach", 0.10, False, False),
        ("grasp", 0.40, False, False),
        ("lift", 0.70, False, False),
        ("drop", 0.20, False, False),
        ("recover", 0.60, False, False),
        ("looks_seated", 0.95, True, False),
        ("verified_seated", 0.98, True, True),
    ]
    writer = csv.writer(sys.stdout)
    writer.writerow([
        "event", "progress", "cost", "progress_delta", "potential_term",
        "base_reward", "combined_reward", "declared_complete", "toy_truth",
    ])
    previous = 0.0
    for name, progress, declared, truth in events:
        term = potential_shaping(previous, progress, terminated=truth)
        base = float(truth)
        writer.writerow([
            name, progress, round(1 - progress, 4), round(progress - previous, 4),
            round(term, 4), base, round(base + term, 4), declared, truth,
        ])
        previous = progress


if __name__ == "__main__":
    main()
