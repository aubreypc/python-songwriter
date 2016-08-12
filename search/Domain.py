import theory.Scale as Scale
import theory.Chord as Chord

"""
Define our default search domains.
"""

ALL_MAJOR_SCALES = [Scale.major_scale() + i for i in range(12)]
# TODO: revisit this --- we don't actually need ALL the major scales,
# if we're modifying the input such that the root note has val 0
TRIADS = [Chord.maj(), Chord.min(), Chord.dim(), Chord.aug()]
SEVENTH_CHORDS = [Chord.maj7(), Chord.min7()]
SUSPENDED_CHORDS = [Chord.sus2(), Chord.sus4()]

DEFAULT_CHORDS = TRIADS + SEVENTH_CHORDS + SUSPENDED_CHORDS #I CAN'T STOP YELLING
