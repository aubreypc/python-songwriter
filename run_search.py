from search import Domain, Sequential
from theory.Note import Note

if __name__ == "__main__":
	input = [Note(0), Note(2)]
	results = Sequential.run(input, Domain.ALL_MAJOR_SCALES)
	for result in results:
		print result.notes
