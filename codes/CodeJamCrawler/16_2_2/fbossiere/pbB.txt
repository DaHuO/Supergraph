temp_res = []
with open("C:/Users/paco/Dropbox/algorithms/google_jam/B-small-attempt2.in") as input_file:
    for i, line in enumerate(input_file):
        if i==0:
            n = int(line)
        else:
            temp_res.append([val for val in line.replace('\n', '').split(" ")])

cases = []
for k, val in enumerate(temp_res):
    cases.append([k+1, val])

import sys
from itertools import product


def get_number(digits):
    if len(digits) == 1:
        return digits[0]
    return 10 * get_number(digits[:-1]) + digits[-1]

def get_number_length(n):
    if n<10:
        return 1
    return 1 + get_number_length(int(n/10))
    
def get_str_number(k, n):
    length_n = get_number_length(n)
    prefix = ''.join(['0'] * (k - length_n))
    return prefix + str(n)


def unfold_combinations(score, combinations, indices):
    candidates = []
    for comb in combinations:
        for i, digit in enumerate(comb):
            score[indices[i]] = str(digit)
        candidates.append(get_number([int(val) for val in score]))
    return candidates


def solve(case):
    coders_score = list(case[1][0])
    number_length = len(coders_score)
    unknown_coders_digits = []
    for i, digit in enumerate(coders_score):
        if digit == '?':
            unknown_coders_digits.append(i)
    
    jammers_score = list(case[1][1])
    unknown_jammers_digits = []
    for i, digit in enumerate(jammers_score):
        if digit == '?':
            unknown_jammers_digits.append(i)
    
    digits = list(range(10))
    coders_combinations = product(digits, repeat=len(unknown_coders_digits))
    coders_candidates = unfold_combinations(coders_score, coders_combinations, unknown_coders_digits)
    jammers_combinations = product(digits, repeat=len(unknown_jammers_digits))
    jammers_candidates = unfold_combinations(jammers_score, jammers_combinations, unknown_jammers_digits)
    
    min_diff = sys.maxint
    min_candidates = set()
    for coder_candidate in coders_candidates:
        for jammers_candidate in jammers_candidates:
            if min_diff > abs(coder_candidate - jammers_candidate):
                min_candidates = {(coder_candidate, jammers_candidate)}
                min_diff = abs(coder_candidate - jammers_candidate)
            if min_diff == abs(coder_candidate - jammers_candidate):
                min_candidates.add((coder_candidate, jammers_candidate))
    if len(min_candidates) == 1:
        return get_str_number(number_length, list(min_candidates)[0][0]) + ' ' + get_str_number(number_length, list(min_candidates)[0][1])
    
    min_coder = sys.maxint
    min_coder_candidates = set()
    for coder_candidate, jammers_candidate in min_candidates:
        if min_coder > coder_candidate:
            min_coder_candidates = {(coder_candidate, jammers_candidate)}
            min_coder = coder_candidate
        if min_coder == coder_candidate:
            min_coder_candidates.add((coder_candidate, jammers_candidate))
    if len(min_coder_candidates) == 1:
        return get_str_number(number_length, list(min_coder_candidates)[0][0]) + ' ' + get_str_number(number_length, list(min_coder_candidates)[0][1])
    
    min_jammer = sys.maxint
    min_jammer_candidates = []
    for coder_candidate, jammers_candidate in min_coder_candidates:
        if min_jammer > jammers_candidate:
            min_jammer_candidates = (coder_candidate, jammers_candidate)
            min_jammer = jammers_candidate
    return get_str_number(
        number_length, min_jammer_candidates[0]) + ' ' + get_str_number(
        number_length, min_jammer_candidates[1])

output_path = "C:/Users/paco/Dropbox/algorithms/google_jam/B-small-attempt2.out"
with open(output_path, mode='w') as output:
    for case in cases:
        answer = solve(case)
        output.write("Case #{i}: ".format(i=case[0]) + str(answer) + '\n')