"""Check mathematical/measurement pitfalls, not research performance."""

import unittest

from signals import completion_summary, potential_shaping


class SignalTests(unittest.TestCase):
    def test_regression_is_not_clipped(self):
        self.assertLess(potential_shaping(0.7, 0.2), 0)

    def test_discounted_terms_telescope(self):
        potentials = [0.2, 0.8, 0.3, 0.9]
        gamma = 0.9
        total = sum(gamma**t * potential_shaping(a, b, gamma)
                    for t, (a, b) in enumerate(zip(potentials, potentials[1:])))
        self.assertAlmostEqual(total, -potentials[0] + gamma**3 * potentials[-1])

    def test_closed_cycle_does_not_pay_positive_bonus(self):
        total = potential_shaping(0.2, 0.8, 1) + potential_shaping(0.8, 0.2, 1)
        self.assertAlmostEqual(total, 0)

    def test_terminal_and_truncation_are_distinct(self):
        self.assertAlmostEqual(potential_shaping(0.7, 0.8, terminated=True), -0.7)
        self.assertAlmostEqual(potential_shaping(0.7, 0.8, terminated=False), 0.092)

    def test_no_declarations_is_not_perfect_verification(self):
        report = completion_summary([False, False], [False, True])
        self.assertIsNone(report["false_completion_among_declarations"])
        self.assertEqual(report["declaration_coverage"], 0)
        self.assertEqual(report["environment_success_rate"], 0.5)

    def test_false_declaration_denominator(self):
        report = completion_summary([True, True, False], [False, True, False])
        self.assertEqual(report["false_completion_among_declarations"], 0.5)
        self.assertAlmostEqual(report["declaration_coverage"], 2 / 3)

    def test_invalid_inputs(self):
        for gamma in (-0.1, 1.1, float("nan")):
            with self.assertRaises(ValueError):
                potential_shaping(0, 1, gamma)
        for decisions, truths in (([], []), ([True], []), ([1], [True])):
            with self.assertRaises(ValueError):
                completion_summary(decisions, truths)


if __name__ == "__main__":
    unittest.main()
