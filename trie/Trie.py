from TrieCursor import TrieCursor

class Trie(object):
    def __init__(self, size):
        self.size = size
        self.root = self.TrieNode(None, size)
        self.cursor = TrieCursor(self)

    class TrieNode(object):
        def __init__(self, val, size, parent=None):
            self.links = [None] * size
            self.val = val
            self.parent = parent

        def __getitem__(self, index):
            return self.links[index]

        def __setitem__(self, index, link):
            if type(link) is self.TrieNode or type(link) is None:
                self.links[index] = link
            else:
                raise Exception("TrieNode can only link to other TrieNodes or to None.")

        def make_child(self, val, index):
            new = self.TrieNode(self, val, size, parent=self)
            self.links[index] = new
            return new

        def has_children(self):
            if True in [link != None for link in self.links]:
                return True
            else:
                return False