from search import Domain, Sequential, Subset
from theory.Note import Note

if __name__ == "__main__":
    input = [Note(2), Note(3)]
    print "Running sequential:"
    results = Sequential.run(input, Domain.ALL_MAJOR_SCALES)
    for result in results:
        print result
    
    print "Running subset:"
    results = Subset.run(input, Domain.ALL_MAJOR_SCALES)
    for result in results:
        print result

