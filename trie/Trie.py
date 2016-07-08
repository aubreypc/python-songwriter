class Trie(object):
    def __init__(self, size):
        self.size = size
        self.root = TrieNode(None, size)

    class TrieNode(object):
        def __init__(self, val, size):
            self.links = [None] * size
            self.val = val

        def __getitem__(self, index):
            return self.links[index]

        def __setitem__(self, index, link):
            if type(link) is TrieNode or type(link) is None:
                self.links[index] = link
            else:
                raise Exception("TrieNode can only link to other TrieNodes or to None.")