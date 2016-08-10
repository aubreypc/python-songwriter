import Domain
	
def run(input, domain):
	#transpose the input to match the domain values
	modifier = input[0].val
	input = [note - modifier for note in input]
	print input
	solutions = []
	for group in domain:
		match = True
		for note in input:
			if note not in group:
				match = False
				break
		if match:
			solutions.append(group)
	return solutions
