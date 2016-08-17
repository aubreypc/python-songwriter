from search import Domain, Sequential, Subset, Substring
from theory.Note import Note
from theory.Scale import Scale, chromatic_scale, DIATONIC_MODES
import argparse

parser = argparse.ArgumentParser(description="Search through musical scales and chords.")
#TODO: actually increase the verbosity
parser.add_argument("-v", "--verbose", help="Enable verbose output", action="store_true")
parser.add_argument("Note", help="A note to search for.", nargs="+")
parser.add_argument("-s", "--scales", help="Add scales to the search domain.", action="store_true")
parser.add_argument("-c", "--chords", help="Add chords to the search domain.", action="store_true")
parser.add_argument("-t", help="The types of searches (sequential/subset) to run.", action="append", dest="searches", default=[])
parser.add_argument("--basic-scales", help="Restrict search results to major and minor scales.", action="store_true", dest="basic_scales", default=False)
parser.add_argument("--basic-chords", help="Restrict search results to major and minor chords.", action="store_true", dest="basic_chords", default=False)

if __name__ == "__main__":
    args = parser.parse_args()
    # convert note args to Note objs
    chrom = map(str, chromatic_scale())
    input = [Note(chrom.index(arg)) for arg in args.Note]
    
    domain = []
    if not args.scales and not args.chords:
        print "Neither chords nor scales selected. Use -s and/or -c. Default behavior is to use both."
        args.scales, args.chords = True, True
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
        additions = []
        for result in results:
            # add relative modes
            if type(result) is Scale:
                if not args.basic_scales:
                    roots = range(1,7)
                    for root in roots:
                        rel = result.relative_mode(root)
                        rel.name = DIATONIC_MODES[root].name
                        additions.append(rel)
                else:
                    rel = result.relative_mode(5)
                    rel.name = DIATONIC_MODES[5].name
                    additions.append(rel)
        results += additions
        for result in results:
            print result
