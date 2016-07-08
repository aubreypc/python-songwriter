class Note(object):
    """
    A single note. Can be defined explicitly or implictly 
    (i.e. a certain interval away from an explicitly defined note).
    """
    def __init__(self, val, octaves_unique=False):
        # note values: A = 1, A#=1 ... G#=12
        # starts at 1 to avoid issues with multiplying/dividing
        self.val = val
        self.octaves_unique = octaves_unique


    """
    The following methods implement transposing using Python's arithmetic operators
    (+, -, /, *, **). Transposition here is explicit, but can be accomplished implicitly, e.g.:
        A = Note(0)
        n = A + 7
    """
    def __add__(self, other):
        if type(other) is Note:
            note = self.val + other.val
        else:
            note = self.val + other
        note = Note(val=note, octaves_unique=self.octaves_unique)
        note.wrap()
        return note

    def __sub__(self, other):
        if type(other) is Note:
            note = self.val - other.val
        else:
            note = self.val - other
        note = Note(val=note, octaves_unique=self.octaves_unique)
        note.wrap()
        return note       

    def __mul__(self, other):
        if type(other) is Note:
            note = self.val * other.val
        else:
            note = self.val * other
        note = Note(val=note, octaves_unique=self.octaves_unique)
        note.wrap()
        return note

    def __div__(self, other):
        if type(other) is Note:
            note = self.val / other.val
        else:
            note = self.val / other
        note = Note(val=note, octaves_unique=self.octaves_unique)
        note.wrap()
        return note

    def __pow__(self, other):
        if type(other) is Note:
            note = self.val ** other.val
        else:
            note = self.val ** other
        note = Note(val=note, octaves_unique=self.octaves_unique)
        note.wrap()
        return note

    def __radd__(self, other):
        if type(other) is Note:
            note = self.val + other.val
        else:
            note = self.val + other
        note = Note(val=note, octaves_unique=self.octaves_unique)
        note.wrap()
        return note

    def __rsub__(self, other):
        if type(other) is Note:
            note = self.val - other.val
        else:
            note = self.val - other
        note = Note(val=note, octaves_unique=self.octaves_unique)
        note.wrap()
        return note
    def __rmul__(self, other):
        if type(other) is Note:
            note = self.val * other.val
        else:
            note = self.val * other
        note = Note(val=note, octaves_unique=self.octaves_unique)
        note.wrap()
        return note

    def __rdiv__(self, other):
        if type(other) is Note:
            note = self.val / other.val
        else:
            note = self.val / other
        note = Note(val=note, octaves_unique=self.octaves_unique)
        note.wrap()
        return note

    def __rpow__(self, other):
        if type(other) is Note:
            note = self.val ** other.val
        else:
            note = self.val ** other
        note = Note(val=note, octaves_unique=self.octaves_unique)
        note.wrap()
        return note

    def __iadd__(self, other):
        if type(other) is Note:
            self.val += other.val
        else:
            self.val += other
        self.wrap()
        return self

    def __isub__(self, other):
        if type(other) is Note:
            self.val -= other.val
        else:
            self.val -= other
        self.wrap()
        return self        

    def __imul__(self, other):
        if type(other) is Note:
            self.val *= other.val
        else:
            self.val *= other
        self.wrap()
        return self

    def __idiv__(self, other):
        if type(other) is Note:
            self.val /= other.val
        else:
            self.val /= other
        self.wrap()
        return self

    def __ipow__(self, other):
        if type(other) is Note:
            self.val **= other.val
        else:
            self.val **= other
        self.wrap()
        return self

    def wrap(self):
        # Do we treat a note as a different note from
        # itself transposed up or down a certain number of octaves?
        # If not, wrap it back around to be between 0 and 12 with mod function
        if not self.octaves_unique:
            if self.val > 12:
                self.val %= 12
            elif self.val == 0:
                self.val = 12
            elif self.val < 0:
                self.val = (self.val * -1) % 12