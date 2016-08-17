from collections import deque
from copy import deepcopy
from theory.Note import Note
from theory.Scale import DIATONIC_MODES

"""
Inspired by substring searches, even if this particular implmentation
isn't *literally* a substring search. (I couldn't think of a better name.)
Essentially, find all the positions in a NoteGroup where the
input intervals line up correctly.
"""

def run(input, domain, verbose=False):
    # Domain should obviously be a lot more limited here
    # than in the other searches --- we only need to find substrings of
    # a single diatonic scale
    modifier = input[0].val
    input = [note - modifier for note in input]
    solutions = []
    for g in domain:
        #we need the octave note for proper substring searching` 
        g.octaves_unique = True
        g.add(12)
        group = g.ordered()
        # find difference between each note in its neighbor
        group_intervals = [group[i+1] - group[i] for i in range(len(group[:-1]))]
        input_intervals = [input[i+1] - input[i] for i in range(len(input[:-1]))]
        
        gen = position_all_intervals(input_intervals, group_intervals, verbose=verbose)
        while True:
            try:
                if verbose:
                    print "Finding another solution."
                start, end = next(gen)
                # if we have found a matching subinterval,
                # we know that the diatonic mode beginning with our first note
                # is a solution
                solution = DIATONIC_MODES[start] + modifier 
                if verbose:
                    print "New solution: mode %d" % start
                    print solution
                solutions.append(solution)
            except StopIteration:
                if verbose:
                    print "Solution not found."
                break
    return solutions

def position_interval(sub_inter, super_inter, verbose=False):
    #generator for finding all positions of our first interval
    dq = deque()
    for index,interval in enumerate(super_inter):
        start_index = index
        dq.append(interval)
        val = sum(dq)
        if verbose:
            print "Index: %d Deque val: %d Target: %d (position_interval)" % (index, val.val, sub_inter.val)
        if val > sub_inter:
            # make space at the front of our deque
            dq.popleft()
            val = sum(dq)
        if val == sub_inter:
            if verbose:
                print "FOUND at position %d" % index
            dq.clear()
            yield (start_index, index) # TODO: we really only need to yield just 1 index

def position_neighbor(sub_inter, super_inter, verbose=False):
    # function to test whether a particular sub-interval can be found
    # at the very beginning of the super-interval
    dq = deque()
    for index,interval in enumerate(super_inter):
        dq.append(interval)
        val = sum(dq)
        if verbose:
            print "Index: %d Deque val: %d Target: %d (position_neighbor)" % (index, val.val, sub_inter.val)
        if val == sub_inter:
            if verbose:
                print "NEIGHBOR FOUND at position %d" % index
            return index
        elif val > sub_inter:
            # if we would have to take something out of the
            # deque in order to get to to the target val later,
            # it is clear that the next match will not be 
            # an immediate neighbor
            return False


def position_all_intervals(sub_inters, super_inter, verbose=False):
    # generator for positioning all intervals
    # position the first, then try positioning neighbors
    # and yield all valid positions
    gen = position_interval(sub_inters[0], super_inter)
    while True:
        try:
            start, end = next(gen)
            if verbose:
                print "Next position: %d" % start
        except StopIteration:
            if verbose:
                print "Outer gen raised StopIteration"
            break
        if len(sub_inters) > 1:
            # we are looking for more than one interval,
            # so make sure that the other target intervals
            # are adjacent to the one we already found
            if verbose:
                print "Finding neighbors"
            match = True
            next_index = start
            for inter in sub_inters[1:]:
                #position the neighbors
                slice_start = next_index
                next_index = position_neighbor(inter, super_inter[slice_start:])
                if next_index is not False:
                    if verbose:
                        print "Neighbor found successfully"
                    # since we found the neighbor, we expand our
                    # list indices to reflect the matching intervals
                    end = next_index + slice_start #TODO: make sure this isnt causing bugs
                    continue
                else:
                    if verbose:
                        print "Neighbor not found."
                    match = False
                    break
            if match:
                if verbose:
                    print "Yielding index: %d" % start
                yield (start,end)
        else:
            print "Yielding index: %d" % start
            yield (start,end)
        
