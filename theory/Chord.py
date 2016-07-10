from NoteGroup import NoteGroup

class Chord(NoteGroup):
    def inversion(self, step):
        return self.starting_with(step)