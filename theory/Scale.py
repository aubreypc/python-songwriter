from NoteGroup import NoteGroup

class Scale(NoteGroup):
    def relative_mode(self, step):
        return self.starting_with(step)
        

def chromatic_scale():
    notes = Scale([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    return notes

def major_scale():
    notes = Scale([0, 2, 4, 5, 7, 9, 11])
    return notes

def ionian_mode():
    return major_scale()

def dorian_mode():
    notes = major_scale().relative_mode(self, 1)

def phrygian_mode():
    notes = major_scale().relative_mode(self, 2)

def lydian_mode():
    notes = major_scale().relative_mode(self, 3)

def mixolydian_mode():
    notes = major_scale().relative_mode(self, 4)

def aeolian_mode():
    notes = major_scale().relative_mode(self, 5)

def minor_scale():
    return aeolian_mode()

def locrian_mode():
    notes = major_scale().relative_mode(self, 6)