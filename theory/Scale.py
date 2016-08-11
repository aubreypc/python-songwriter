from Note import Note
from NoteGroup import NoteGroup

class Scale(NoteGroup):
    def __init__(self, *args, **kwargs):
	    super(Scale, self).__init__(*args, group_type_name="scale", **kwargs)

    def relative_mode(self, step):
        return Scale(self.notes, root=step)

    def __add__(self, other):
        # transpose with + operator
        s = Scale([note.val + other for note in self.notes])
        if self.root:
            s.root = Note(self.root.val + other)
        return s

    def __sub__(self, other):
        #transpose with - operator
        s = Scale([note.val - other for note in self.notes])
        if self.root:
            s.root = Note(self.root.val + other)
        return s


def chromatic_scale():
    notes = Scale([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], name="chromatic", root=0)
    return notes

def major_scale():
    notes = Scale([0, 2, 4, 5, 7, 9, 11], name="ionian (major)", root=0)
    return notes

def ionian_mode():
    return major_scale()

def dorian_mode():
    notes = major_scale().relative_mode(1)
    notes.name = "dorian"
    return notes

def phrygian_mode():
    notes = major_scale().relative_mode(2)
    notes.name = "phrygian"
    return notes

def lydian_mode():
    notes = major_scale().relative_mode(3)
    notes.name = "lydian"
    return notes

def mixolydian_mode():
    notes = major_scale().relative_mode(4)
    notes.name = "mixolydian"
    return notes

def aeolian_mode():
    notes = major_scale().relative_mode(5)
    notes.name = "aeolian (minor)"
    return notes

def minor_scale():
    return aeolian_mode()

def locrian_mode():
    notes = major_scale().relative_mode(6)
    notes.name = "locrian"
    return notes
