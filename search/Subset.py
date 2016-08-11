import Domain

def run(input, domain):
    #transpose the input to match the domain values
    modifier = input[0].val
    input = set([note - modifier for note in input])
    solutions = []
    for group in domain:
        if input.issubset(group.notes):
            solutions.append(group + modifier)
    return solutions
