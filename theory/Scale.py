from NoteGroup import NoteGroup

class Scale(NoteGroup):
    def relative_mode(self, step):
        return Scale(self.starting_with(step))
        

def chromatic_scale():
    notes = Scale([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    return notes

def major_scale():
    notes = Scale([0, 2, 4, 5, 7, 9, 11])
    return notes

def ionian_mode():
    return major_scale()

def dorian_mode():
    notes = major_scale().relative_mode(1)
    return notes

def phrygian_mode():
    notes = major_scale().relative_mode(2)
    return notes

def lydian_mode():
    notes = major_scale().relative_mode(3)
    return notes

def mixolydian_mode():
    notes = major_scale().relative_mode(4)
    return notes

def aeolian_mode():
    notes = major_scale().relative_mode(5)
    return notes

def minor_scale():
    return aeolian_mode()

def locrian_mode():
    notes = major_scale().relative_mode(6)
    return notes
