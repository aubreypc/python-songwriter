import unittest
from theory.Note import Note

class NoteTests(unittest.TestCase):
    def test_transposing(self):
        A = Note(1)
        self.assertEqual(A.val, 1)

        A_sharp = A + 1
        self.assertEqual(A_sharp.val, 2)

        A2 = A_sharp - 1
        self.assertEqual(A2.val, A.val)

    def test_transposing_assignment(self):
        n = Note(1)
        n += 1
        self.assertEqual(n.val, 2)
        n -= 1
        self.assertEqual(n.val, 1)

    def test_wrapping(self):
        n = Note(13, octaves_unique=False)
        n.wrap()
        self.assertEqual(n.val, 1)

        n.val = 0
        n.wrap()
        self.assertEqual(n.val, 12)

        n2 = Note(13, octaves_unique=True)
        n2.wrap()
        self.assertEqual(n2.val, 13)

        n2.val = 0
        n2.wrap()
        self.assertEqual(n2.val, 0)


if __name__ == "__main__":
    unittest.main()