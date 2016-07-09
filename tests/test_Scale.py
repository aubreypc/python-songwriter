import unittest
from sets import Set
from theory.Scale import Scale

class ScaleTests(unittest.TestCase):
    def test_get_steps(self):
        s = Scale(Set([2, 4, 0]))
        steps = s.get_steps()
        self.assertTrue(type(steps) is list)
        self.assertTrue(len(steps) == len(s.notes))
        for step in steps:
            self.assertTrue(step in s.notes)

    def test_relative_mode(self):
        s = Scale(Set([0, 2, 4]))
        s_steps = s.get_steps()
        rel = s.relative_mode(1)
        self.assertTrue(len(rel) == len(s_steps))
        self.assertTrue(rel[0] == 2)
        self.assertTrue(rel[1] == 4)
        self.assertTrue(rel[2] == 0)

if __name__ == "__main__":
    unittest.main()