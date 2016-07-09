from sets import Set
from Note import Note

class NoteGroup(object):
    """
    A group of notes. Base class for Scales and Chords.
    """
    def __init__(self, vals=None, octaves_unique=False):
        self.notes = Set()
        self.octaves_unique = octaves_unique
        if vals:
            self.add(vals)

    def __iter__(self):
        return iter(self.notes)

    def __eq__(self, other):
        vals = [note.val for note in self.notes]
        other_vals = [note.val for note in other.notes]
        if len(vals) != len(other_vals):
            return False
        for val in vals:
            if val not in other_vals:
                return False
        return True

    def add(self, note):
        # when adding to a NoteGroup, we need to make sure
        # that the object we're adding is of type Note
        # sometimes dynamically typed languages can be a headache
        if type(note) is Set:
            elem = note.pop()
            if type(elem) is Note:
                note.add(elem)
                self.notes.update(note)
            else:
                note.add(elem)
                converted = [Note(elem, octaves_unique=self.octaves_unique) for elem in note]
                self.notes.update(Set(converted))
        elif type(note) is list:
            converted = []
            for elem in note:
                if type(elem) is Note:
                    converted.append(elem)
                else:
                    converted.append(Note(elem, octaves_unique=self.octaves_unique))
            self.notes.update(Set(converted))
        elif type(note) is int:
            self.notes.update(Set([Note(note, octaves_unique=self.octaves_unique)]))
        else:
            self.notes.update(Set([note]))
        return self.notes

    def ordered(self):
        #represent group as a list, ordered by value
        steps = [note for note in self.notes]
        steps.sort()
        return steps

    def remove(self, note):
        self.notes.remove(note)
        return self.notes

    def relative_to(self, root):
        #given a root note and a NoteGroup of intervals, 
        #return the NoteGroup which has the relative notes explicitly defined
        notes = Set([root + interval for interval in self.notes])
        return NoteGroup(notes)