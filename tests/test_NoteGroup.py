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
        self.assertFalse(g != g2)

        g2.add(Note(2))
        self.assertFalse(g == g2)
        self.assertTrue(g != g2)

    def test_ordered(self):
        g = NoteGroup(Set([2, 4, 0]))
        steps = g.ordered()
        self.assertTrue(type(steps) is list)
        self.assertTrue(len(steps) == len(g.notes))
        for step in steps:
            self.assertTrue(step in g.notes)
        
        root_note = Note(2)
        n2 = Note(4)
        n3 = Note(0)
        g2 = NoteGroup(Set([n2, n3, root_note]), root=root_note)
        steps2 = g2.ordered()
        self.assertTrue(steps2[0] == root_note)
        self.assertTrue(steps2[1] == n2)
        self.assertTrue(steps2[2] == n3)


    def test_starting_with(self):
        g = NoteGroup(Set([0, 2, 4]))
        g_steps = g.ordered()
        rel = g.starting_with(1)
        self.assertTrue(len(rel) == len(g_steps))
        self.assertTrue(rel[0] == 2)
        self.assertTrue(rel[1] == 4)
        self.assertTrue(rel[2] == 0)

    def test_contains(self):
	g = NoteGroup(Set([0, 2]))
	self.assertTrue(Note(0) in g)
	self.assertTrue(Note(2) in g)
	self.assertTrue(Note(4) not in g)

if __name__ == "__main__":
    unittest.main()
