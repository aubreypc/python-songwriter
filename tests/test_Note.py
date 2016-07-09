import unittest
from theory.Note import Note

class NoteTests(unittest.TestCase):
    def test_transposing(self):
        n = Note(1)
        self.assertEqual(n.val, 1)

        n2 = n + 1
        self.assertEqual(n2.val, 2)

        n3 = n2 - 1
        self.assertEqual(n3.val, n.val)

    def test_transposing_assignment(self):
        n = Note(1)
        n += 1
        self.assertEqual(n.val, 2)
        n -= 1
        self.assertEqual(n.val, 1)

    def test_wrapping(self):
        n = Note(12, octaves_unique=False)
        self.assertEqual(n.val, 0)

        n.val = 0
        n.wrap()
        self.assertEqual(n.val, 0)

        n2 = Note(12, octaves_unique=True)
        self.assertEqual(n2.val, 12)

        n2.val = 0
        n2.wrap()
        self.assertEqual(n2.val, 0)

    def test_comparison(self):
        a = Note(1)
        a2 = Note(1)
        b = Note(3)

        self.assertTrue(a == a2)
        self.assertFalse(a == b)

        self.assertTrue(a < b)
        self.assertFalse(a > b)

        #what about things with other types?
        a3 = 1
        b2 = 3

        self.assertTrue(a3 == a)
        self.assertFalse(b2 == a)



if __name__ == "__main__":
    unittest.main()