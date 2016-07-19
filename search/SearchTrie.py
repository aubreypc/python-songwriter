from trie.Trie import Trie
from theory.Note import Note
from theory.Scale import *

class SearchTrie(object):
    def __init__(self):
        self.trie = self.build()

    def build():
        t = Trie(13)
        groups = self.all_searchable_groups()
        for root_note in chromatic_scale():
            relative_groups = groups.relative_to(root_note)
            for group in relative_groups:
                t.new_cursor() #reset back to root node
                for note in group:
                    if note not in t.current.links:
                        t.current.make_child(note, note.val)
                        t.travel(note.val)
                # add an "end of search" indicator
                t.current.make_child(repr(group), 13)
        return t


    def all_searchable_groups(self):
        # all the scales and chords
        # which should be put into our tries
        return [
            ionian_mode(),
            dorian_mode(),
            phrygian_mode(),
            lydian_mode(),
            mixolydian_mode(),
            aeolian_mode(),
            locrian_mode(),
        ]