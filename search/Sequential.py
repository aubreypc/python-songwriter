import Domain
	
def run(input, domain):
    #transpose the input to match the domain values
    print input
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
            solutions.append(group + modifier)
            if domain == Domain.ALL_MAJOR_SCALES:
                # add relative diatonic modes
                modes = ["ionian (major)", "dorian", "phrygian", "lydian", "mixolydian", 
                        "aeolian (minor)", "locrian"]
                for i in range(2, 7):
                    mode = group.relative_mode(i)
                    mode.name = modes[i]
                    solutions.append(mode + modifier)
    return solutions
