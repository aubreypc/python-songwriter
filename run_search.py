from search import Domain, Sequential, Subset, Substring
from theory.Note import Note
from theory.Scale import chromatic_scale
import argparse

parser = argparse.ArgumentParser(description="Search through musical scales and chords.")
#TODO: actually increase the verbosity
parser.add_argument("-v", "--verbose", help="Enable verbose output", action="store_true")
parser.add_argument("Note", help="A note to search for.", nargs="+")
parser.add_argument("-s", "--scales", help="Add scales to the search domain.", action="store_true")
parser.add_argument("-c", "--chords", help="Add chords to the search domain.", action="store_true")
parser.add_argument("-t", help="The types of searches (sequential/subset) to run.", action="append", dest="searches", default=[])

if __name__ == "__main__":
    args = parser.parse_args()
    # convert note args to Note objs
    chrom = map(str, chromatic_scale())
    input = [Note(chrom.index(arg)) for arg in args.Note]
    
    domain = []
    if args.scales:
        domain += Domain.ALL_MAJOR_SCALES
    if args.chords:
        domain += Domain.DEFAULT_CHORDS
    default_search = "sequential" #TODO: change to whichever is faster

    if len(args.searches) == 0:
        args.searches.append(default_search)
    for search in args.searches:
        if search.lower() == "sequential":
            results = Sequential.run(input, domain)
        elif search.lower() == "subset":
            results = Subset.run(input, domain)
        elif search.lower() == "substring":
            #since domains work a little differently here
            results = []
            if args.scales:
                results += Substring.run(input, Domain.ONE_DIATONIC_SCALE, verbose=args.verbose)
        else:
            raise Exception("Invalid search type: " + search)
        if args.verbose:
            print "Ran %s search." % search
        print "Search results:"
        for result in results:
            print result

