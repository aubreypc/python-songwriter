import unittest
from sets import Set
from theory.Scale import Scale

class NoteGroupTests(unittest.TestCase):
    def test_get_steps():
        s = Scale(Set([2, 4, 0]))
        steps = s.get_steps()
        self.assertTrue(type(steps) is list)
        self.assertTrue(steps == [0, 2, 4])

    def test_relative_mode():
        s = Scale(Set([0, 2, 4, 11]))
        rel = s.relative_mode(1)
        steps = rel.get_steps()
        self.assertTrue(steps == [2, 4, 11, 0])

if __name__ == "__main__":
    unittest.main()