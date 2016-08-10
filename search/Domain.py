from theory.Scale import *
from theory.Chord import *

"""
Define our default search domains.
"""

ALL_MAJOR_SCALES = [major_scale().relative_to(i) for i in range(12)]