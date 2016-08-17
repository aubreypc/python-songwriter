usage: run_search.py [-h] [-v] [-s] [-c] [-t SEARCHES] [--basic-scales]
                     [--basic-chords]
                     Note [Note ...]

Search through musical scales and chords.

positional arguments:
  Note            A note to search for.

optional arguments:
  -h, --help      show this help message and exit
  -v, --verbose   Enable verbose output
  -s, --scales    Add scales to the search domain.
  -c, --chords    Add chords to the search domain.
  -t SEARCHES     The types of searches (sequential/subset) to run.
  --basic-scales  Restrict search results to major and minor scales.
  --basic-chords  Restrict search results to major and minor chords.
