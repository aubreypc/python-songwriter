from sets import Set
from Note import Note

class NoteGroup(object):
    """
    A group of notes. Base class for Scales and Chords.
    """
    def __init__(self, vals=None):
        self.notes = vals

    def add(self, note):
        if type(note) is Set:
            self.notes.update(note)
        else:
            self.notes.update(Set(note))
        return self.notes

    def remove(self, note):
        self.notes.remove(note)
        return self.notes

    def relative_to(self, root):
        #given a root note and a NoteGroup of intervals, 
        #return the NoteGroup which has the relative notes explicitly defined
        notes = Set([root + interval for interval in self.notes])
        return notes