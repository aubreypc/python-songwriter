import unittest
from trie.Trie import Trie
from trie.TrieCursor import TrieCursor

class TrieTests(unittest.TestCase):
    def test_make_child(self):
        t = Trie(2)
        child = t.root.make_child(1, 0)
        self.assertTrue(t.root.links[0] is child)
        self.assertTrue(t.root.links[0].val == 1)

    def test_cursor(self):
        t = Trie(2)

        t.root.val = 1
        node2 = t.root.make_child(2, 0)
        node3 = node2.make_child(3, 1)
        
        current = t.travel(0)
        self.assertTrue(current is node2)

        current = t.travel(1)
        self.assertTrue(current is node3)

        current = t.travel(-1)
        self.assertTrue(current is node2)

        with self.assertRaises(StopIteration):
            t.travel(1)
            t.travel(1)

if __name__ == "__main__":
    unittest.main()