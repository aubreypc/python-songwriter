from TrieCursor import TrieCursor

class Trie(object):
    def __init__(self, size):
        self.size = size
        self.root = self.TrieNode(None, size)
        self.new_cursor()

    def generator(self):
        while True:
            self.target_link = yield
            if not self.current.has_children():
                break
            self.current = self.current.links[self.target_link]
            yield self.current

    def new_cursor(self):
        self.current = self.root
        self.cursor = self.generator()
        return self.cursor

    def travel(self, next_link):
        self.cursor.next()
        return self.cursor.send(next_link)

    class TrieNode(object):
        def __init__(self, val, size, parent=None):
            self.links = [None] * size
            self.size = size
            self.val = val
            self.parent = parent

        def __getitem__(self, index):
            return self.links[index]

        def __setitem__(self, index, link):
            if type(link) is TrieNode or type(link) is None:
                self.links[index] = link
            else:
                raise Exception("TrieNode can only link to other TrieNodes or to None.")

        def make_child(self, val, index):
            new = self.__class__(val, self.size, parent=self)
            self.links[index] = new
            return new

        def has_children(self):
            if True in [link != None for link in self.links]:
                return True
            else:
                return False