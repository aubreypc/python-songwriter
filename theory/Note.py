class Note(object):
    """
    A single note. Can be defined explicitly or implictly 
    (i.e. a certain interval away from an explicitly defined note).
    """
    def __init__(self, val, octaves_unique=True):
        # note values: A = 0, A#=1 ... G#=12
        self.val = val
        self.octaves_unique = octaves_unique


    """
    The following methods implement transposing using Python's arithmetic operators
    (+, -, /, *, **, %). Transposition here is explicit, but can be accomplished implicitly, e.g.:
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

    def __mod__(self, other):
        if type(other) is Note:
            note = self.val % other.val
        else:
            note = self.val % other
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

    def __rmod__(self, other):
        if type(other) is Note:
            note = self.val % other.val
        else:
            note = self.val % other
        note = Note(val=note, octaves_unique=self.octaves_unique)
        note.wrap()
        return note

    def __add__(self, other):
        if type(other) is Note:
            self.val += other.val
        else:
            self.val += other
        self.wrap()
        return self

    def __sub__(self, other):
        if type(other) is Note:
            self.val -= other.val
        else:
            self.val -= other
        self.wrap()
        return self        

    def __mul__(self, other):
        if type(other) is Note:
            self.val *= other.val
        else:
            self.val *= other
        self.wrap()
        return self

    def __div__(self, other):
        if type(other) is Note:
            self.val /= other.val
        else:
            self.val /= other
        self.wrap()
        return self

    def __pow__(self, other):
        if type(other) is Note:
            self.val **= other.val
        else:
            self.val **= other
        self.wrap()
        return self

    def __mod__(self, other):
        if type(other) is Note:
            self.val %= other.val
        else:
            self.val %= other
        self.wrap()
        return self

    def wrap(self):
        # Do we treat a note as a different note from
        # itself transposed up or down a certain number of octaves?
        # If not, wrap it back around to be between 0 and 12 with mod function
        if not self.octaves_unique:
            self.val %= 12