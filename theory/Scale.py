from NoteGroup import NoteGroup

class Scale(NoteGroup):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)

    def get_steps(self):
        #since scales are ordered, we want a list representation
        steps = [note for note in self.notes]
        sort(steps)
        return steps

    def relative_mode(self, step):
        #same notes, rearranged to have a different root
        #it pains me to start the mode indices at 0 but
        #that is the way we roll in computer science
        if step == 0:
            return self
        else:
            steps = self.get_steps()
            notes = note + steps[step:] + steps[:step]
            return Scale(Set(notes))
        

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