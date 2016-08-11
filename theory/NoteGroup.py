from sets import Set
from Note import Note

class NoteGroup(object):
    """
    A group of notes. Base class for Scales and Chords.
    """
    def __init__(self, vals=None, root=None, octaves_unique=False, name=None, group_type_name=None):
        self.notes = Set()
        self.octaves_unique = octaves_unique
        if type(root) is int:
            self.root = Note(root)
        else:
            self.root = root
        if vals:
            self.add(vals)
        self.name = name
        self.group_type_name = group_type_name

    def __iter__(self):
        return iter(self.notes)

    def __repr__(self):
        if self.name and self.group_type_name:
		    return "{} {} {}: {}".format(
		        str(self.ordered()[0]),
		        self.name,
		        self.group_type_name,
		        [str(n) for n in self.ordered()],
		    )
        elif self.group_type_name:
		    return "{}: {}".format(
		        self.group_type_name,
		        [str(n) for n in self.ordered()],
            )
        else:
            return "Note group: " + [str(n) for n in self.ordered()]    

    def __eq__(self, other):
        vals = [note.val for note in self.notes]
        other_vals = [note.val for note in other.notes]
        if len(vals) != len(other_vals):
            return False
        for val in vals:
            if val not in other_vals:
                return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def add(self, note):
        # when adding to a NoteGroup, we need to make sure
        # that the object we're adding is of type Note
        # sometimes dynamically typed languages can be a headache
        if type(note) is list or type(note) is Set:
            for elem in note:
                if type(elem) is Note:
                    converted = elem
                else:
                    converted = Note(elem, octaves_unique=self.octaves_unique)
                self.add(converted)
        elif type(note) is int:
            self.add(Note(note, octaves_unique=self.octaves_unique))
        elif type(note) is Note:
            self.notes.update(Set([note]))
            if not self.root:
                self.root = note
        else:
            self.notes.update(Set([note]))
        return self.notes

    def ordered(self):
        #represent group as a list, ordered by value
        steps = [note for note in self.notes]
        steps.sort()
        if self.root:
            root_index = steps.index(self.root)
            steps = steps[root_index:] + steps[:root_index]
        return steps

    def starting_with(self, step):
        #same notes, rearranged to have a different root
        if step == 0:
            return self
        else:
            steps = self.ordered()
            notes = steps[step:] + steps[:step]
            return notes

    def remove(self, note):
        self.notes.remove(note)
        return self.notes

    def relative_to(self, root):
        #given a root note and a NoteGroup of intervals, 
        #return the NoteGroup which has the relative notes explicitly defined
        notes = Set([root + interval for interval in self.notes])
        return NoteGroup(notes)
