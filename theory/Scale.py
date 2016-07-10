from NoteGroup import NoteGroup

class Scale(NoteGroup):
    def relative_mode(self, step):
        return self.starting_with(step)
        

def chromatic():
    notes = Scale([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    return notes

def major():
    notes = Scale([0, 2, 4, 5, 7, 9, 11])
    return notes

def ionian():
    return major()

def dorian():
    notes = major().relative_mode(self, 1)

def phrygian():
    notes = major().relative_mode(self, 2)

def lydian():
    notes = major().relative_mode(self, 3)

def mixolydian():
    notes = major().relative_mode(self, 4)

def aeolian():
    notes = major().relative_mode(self, 5)

def minor():
    return aeolian()

def locrian():
    notes = major().relative_mode(self, 6)