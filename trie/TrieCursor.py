class TrieCursor(object):
    """
    Object which handles traversing tries.
    """
    def __init__(self, trie):
        self.trie = trie
        self.current = trie.root

    def travel(self, link):
        while self.current.has_children():
            self.current = current[link]
            yield self.current.val