#!/usr/bin/python

import sys

def idx_to_party_str(idx):
    return chr(ord("A") + idx)

def find_largest(parties):
    max_one = 0
    max_one_idx = -1
    max_two = 0
    max_two_idx = -1
    max_three = 0
    max_three_idx = -1
    for idx, p in enumerate(parties):
        if p > max_one:
            max_one = p
            max_one_idx = idx
            continue
        if p > max_two:
            max_two = p
            max_two_idx = idx
            continue
        if p > max_three:
            max_three = p
            max_three_idx = idx
            continue

    return [max_one, max_one_idx, max_two, max_two_idx, max_three, max_three_idx]


def solve(party_c, parties):
    result = ""
    while True:
        largest_idx = find_largest(parties)
        if largest_idx[0] == 1 and largest_idx[2] == 1 and largest_idx[4] == 1:
            result += idx_to_party_str(largest_idx[1])
            parties[largest_idx[1]] -= 1
        elif largest_idx[0] == largest_idx[2]:
            result += idx_to_party_str(largest_idx[1])
            result += idx_to_party_str(largest_idx[3])
            parties[largest_idx[1]] -= 1
            parties[largest_idx[3]] -= 1
        else:
            result += idx_to_party_str(largest_idx[1])
            parties[largest_idx[1]] -= 1

        done = True
        for p in parties:
            if p > 0:
                done = False
                break

        if done:
            return result

        result += " "

lines = open(sys.argv[1], "rt").readlines()

test_cases_c = int(lines[0])

lines = lines[1:]

for i in xrange(test_cases_c):
    print "Case #"+str(i+1)+":",
    party_c = int(lines[0])
    parties = lines[1].split()
    parties = [int(p) for p in parties]
    lines = lines[2:]
    print solve(party_c, parties)
