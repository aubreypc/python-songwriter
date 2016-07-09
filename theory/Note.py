class Note(object):
    """
    A single note. Can be defined explicitly or implictly 
    (i.e. a certain interval away from an explicitly defined note).
    """
    def __init__(self, val, octaves_unique=False):
        # note values: A=0, A#=1 ... G#=11
        self.val = val
        self.octaves_unique = octaves_unique
        self.wrap()

    def __str__(self):
        chromatic = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
        if self.octaves_unique and self.val > 11:
            return chromatic[self.val % 12]
        else:
            return chromatic[self.val]

    def __repr__(self):
        return "Note with val %d (%s)" % (self.val, self.__str__())


    """
    The following methods implement transposing using Python's arithmetic operators
    (+, -). Multiplication, division, power, and mod left out to avoid issues with 0,
    and because they would probably never be used.
    Transposition here is explicit, but can be accomplished implicitly, e.g.:
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

    """
    Comparison methods (==, >, >=, <, <=)
    """
    def __eq__(self, other):
        if type(other) is Note:
            return self.val == other.val
        else:
            return self.val == other
    
    def __gt__(self, other):
        if type(other) is Note:
            return self.val > other.val
        else:
            return self.val > other

    def __ge__(self, other):
        if type(other) is Note:
            return self.val >= other.val
        else:
            return self.val >= other

    def __lt__(self, other):
        if type(other) is Note:
            return self.val < other.val
        else:
            return self.val < other

    def __le__(self, other):
        if type(other) is Note:
            return self.val <= other.val
        else:
            return self.val <= other

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