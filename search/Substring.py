from collections import deque

"""
Inspired by substring searches, even if this particular implmentation
isn't *literally* a substring search. (I couldn't think of a better name.)
Essentially, find all the positions in a NoteGroup where the
input intervals line up correctly.
"""

def run(input, domain):
    # Domain should obviously be a lot more limited here
    # than in the other searches --- we only need to find substrings of
    # a single diatonic scale
    modifier = input[0].val
    input = [note - modifier for note in input]
    solutions = []
    for group in domain:
        #we need the octave note for proper substring searching` 
        group.octaves_unique = True
        group.add(12)
        group = group.ordered()
        # find difference between each note in its neighbor
        group_intervals = [group[i+1] - group[i] for i in range(len(group[:-1]))]
        input_intervals = [input[i+1] - input[i] for i in range(len(input[:-1]))]
        for target_interval in input_intervals:
            dq = deque()
            print target_interval
            for index,interval in enumerate(group_intervals):
                print index
                dq.append(interval)
                print dq
                val = sum(dq)
                if val == target_interval:
                    print "FOUND at position %d" % index
                    #TODO: do something with this knowledge
                    dq.clear()
                elif val > target_interval:
                    # make space at the front of our deque
                    dq.popleft()
                    print "Popped left"
    return solutions
