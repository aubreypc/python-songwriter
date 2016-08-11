from NoteGroup import NoteGroup

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
