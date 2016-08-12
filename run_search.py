from search import Domain, Sequential, Subset
from theory.Note import Note
from theory.Scale import chromatic_scale
import argparse

parser = argparse.ArgumentParser(description="Search through musical scales and chords.")
#TODO: actually increase the verbosity
parser.add_argument("-v", "--verbose", help="Enable verbose output", action="store_true")
parser.add_argument("Notes", help="The group of notes to search for.", nargs="+")

if __name__ == "__main__":
    args = parser.parse_args()
    # convert note args to Note objs
    chrom = map(str, chromatic_scale())
    input = [Note(chrom.index(arg)) for arg in args.Notes]

    print "Running sequential:"
    results = Sequential.run(input, Domain.ALL_MAJOR_SCALES)
    for result in results:
        print result
    
    print "Running subset:"
    results = Subset.run(input, Domain.ALL_MAJOR_SCALES)
    for result in results:
        print result

