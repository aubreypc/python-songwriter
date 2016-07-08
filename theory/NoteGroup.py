from sets import Set
from Note import Note

class NoteGroup(object):
    """
    A group of notes. Base class for Scales and Chords.
    """
    def __init__(self, vals=None):
        self.notes = vals

    def __getitem__(self, index):
        if type(self.notes) is list:
            return self.notes[index]

    def add(self, note):
        if type(self.notes) is list: #for ordered groups
            if type(note) is int and note not in self.notes: #just one note as input, not a collection
                self.notes.append(note)
            else:
                for n in note:
                    if note not in self.notes:
                        self.notes.append(n)
            sort(self.notes)
        elif type(self.notes) is Set: #for unordered groups
            self.notes.update(Set(note))
        return self.notes

    def remove(self, note):
        self.notes.remove(note)
        return self.notes

    def relative_to(self, root):
        #given a root note and a NoteGroup of intervals, 
        #return the NoteGroup which has the relative notes explicitly defined
        notes = [note + interval for interval in self.notes]
        if type(self.notes) is Set:
            notes = Set(notes)
        return notes