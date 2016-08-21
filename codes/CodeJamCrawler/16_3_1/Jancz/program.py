#!/usr/bin/env python

from sys import argv
import operator


def getInvalidIndices(politicans_per_party, remaining_politicans):
    remaining_politicans = float(remaining_politicans)
    vote_power = [value / remaining_politicans for value in politicans_per_party]
    return [index for index, value in enumerate(vote_power) if value > 0.50]


def solve(politicans_per_party):
    removed_politicans = []
    while max(politicans_per_party) > 0:
        remaining_politicans = sum(politicans_per_party)

        remaining_politicans, index = method_name(politicans_per_party, remaining_politicans)
        first_removed_politican = chr(65 + index)

        invalid_indices = getInvalidIndices(politicans_per_party, remaining_politicans)
        if len(invalid_indices) == 1:
            remaining_politicans, index = method_name(politicans_per_party, remaining_politicans)
            second_removed_politican = chr(65 + index)
            removed_politicans.append(first_removed_politican + second_removed_politican)
        else:
            removed_politicans.append(first_removed_politican)

    return ' '.join(removed_politicans)


def method_name(politicans_per_party, remaining_politicans):
    index, value = max(enumerate(politicans_per_party), key=operator.itemgetter(1))
    politicans_per_party[index] -= 1
    remaining_politicans -= 1
    return remaining_politicans, index


with open(argv[1], 'r') as input_file:
    number_of_cases = int(input_file.readline())
    for current_case_number in range(1, number_of_cases + 1):
        number_of_political_parties = int(input_file.readline())
        politicans_per_party = input_file.readline().strip().split(' ')
        politicans_per_party = [int(x) for x in politicans_per_party]
        print('Case #%i: %s' % (current_case_number, solve(politicans_per_party)))
