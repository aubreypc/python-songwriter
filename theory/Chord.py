from NoteGroup import NoteGroup

class Chord(NoteGroup):
    def __init__(self, *args, **kwargs):
        super(Chord, self).__init__(*args, group_type_name="chord", **kwargs)

    def inversion(self, step):
        return Chord(self.notes, root=step)
