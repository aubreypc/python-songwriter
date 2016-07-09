import unittest
from sets import Set
from theory.Note import Note
from theory.NoteGroup import NoteGroup

class NoteGroupTests(unittest.TestCase):
    def test_adding_removing(self):
        g = NoteGroup()
        n = Note(0)
        g.add(n)
        self.assertTrue(n in g)

        g.remove(n)
        self.assertFalse(n in g)

    def test_type_checking(self):
        g = NoteGroup()
        n = Note(1)
        n2 = 2
        g.add(n)
        g.add(n2)
        for note in g:
            self.assertTrue(type(note) is Note)

    def test_relative_transposing(self):
        g = NoteGroup()
        n = Note(0)
        n2 = Note(1)
        g.add(Set([n, n2]))
        g2 = g.relative_to(2)
        self.assertTrue(len(g2.notes) == 2)
        self.assertTrue(2 in g2)
        self.assertTrue(3 in g2)

    def test_comparison(self):
        g = NoteGroup()
        g2 = NoteGroup()
        n = Note(1)
        g.add(Note(1))
        g2.add(Note(1))
        self.assertTrue(g == g2)

        g2.add(Note(2))
        self.assertFalse(g == g2)

if __name__ == "__main__":
    unittest.main()