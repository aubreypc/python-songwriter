from NoteGroup import NoteGroup
from Note import Note

class Chord(NoteGroup):
    def __init__(self, *args, **kwargs):
        super(Chord, self).__init__(*args, group_type_name="chord", **kwargs)

    def inversion(self, step):
        return Chord(self.notes, root=step)

    def __add__(self, other):
        # transpose with + operator
        s = Chord([note.val + other for note in self.notes], name=self.name)
        if self.root:
            s.root = Note(self.root.val + other)
        return s

    def __sub__(self, other):
        #transpose with - operator
        s = Chord([note.val - other for note in self.notes])
        if self.root:
            s.root = Note(self.root.val + other)
        return s

def maj():
    return Chord([0, 4, 7], name="Major triad")

def maj7():
    return Chord([0, 4, 7, 11], name="Major 7")

def min():
    return Chord([0, 3, 7], name="Minor triad")

def min7():
    return Chord([0, 3, 7, 11], name="Minor 7")

def dim():
    return Chord([0, 3, 6], name="Diminished triad")

def aug():
    return Chord([0, 4, 8], name="Augmented triad")

def sus2():
    return Chord([0, 2, 7], name="Suspended 2nd")

def sus4():
    return Chord([0, 5, 7], name="Suspended 4th")


