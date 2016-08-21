#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solve(s):
    dictionary = dict()
    for c in s:
        dictionary[c] = dictionary.get(c, 0) + 1
    num_dict = [0 for _ in range(10)]
    num_dict[0] = dictionary.get('Z', 0)
    if num_dict[0] > 0:
        dictionary['Z'] -= num_dict[0]
        dictionary['E'] -= num_dict[0]
        dictionary['R'] -= num_dict[0]
        dictionary['O'] -= num_dict[0]
    num_dict[2] = dictionary.get('W', 0)
    if num_dict[2] > 0:
        dictionary['T'] -= num_dict[2]
        dictionary['W'] -= num_dict[2]
        dictionary['O'] -= num_dict[2]
    num_dict[4] = dictionary.get('U', 0)
    if num_dict[4] > 0:
        dictionary['F'] -= num_dict[4]
        dictionary['O'] -= num_dict[4]
        dictionary['U'] -= num_dict[4]
        dictionary['R'] -= num_dict[4]
    num_dict[6] = dictionary.get('X', 0)
    if num_dict[6] > 0:
        dictionary['S'] -= num_dict[6]
        dictionary['I'] -= num_dict[6]
        dictionary['X'] -= num_dict[6]
    num_dict[8] = dictionary.get('G', 0)
    if num_dict[8] > 0:
        dictionary['E'] -= num_dict[8]
        dictionary['I'] -= num_dict[8]
        dictionary['G'] -= num_dict[8]
        dictionary['H'] -= num_dict[8]
        dictionary['T'] -= num_dict[8]
    num_dict[3] = dictionary.get('T', 0)
    if num_dict[3] > 0:
        dictionary['T'] -= num_dict[3]
        dictionary['H'] -= num_dict[3]
        dictionary['R'] -= num_dict[3]
        dictionary['E'] -= num_dict[3]
        dictionary['E'] -= num_dict[3]
    num_dict[5] = dictionary.get('F', 0)
    if num_dict[5] > 0:
        dictionary['F'] -= num_dict[5]
        dictionary['I'] -= num_dict[5]
        dictionary['V'] -= num_dict[5]
        dictionary['E'] -= num_dict[5]
    num_dict[7] = dictionary.get('S', 0)
    if num_dict[7] > 0:
        dictionary['S'] -= num_dict[7]
        dictionary['E'] -= num_dict[7]
        dictionary['V'] -= num_dict[7]
        dictionary['E'] -= num_dict[7]
        dictionary['N'] -= num_dict[7]
    num_dict[1] = dictionary.get('O', 0)
    num_dict[9] = dictionary.get('I', 0)
    result = ''
    for i, num in enumerate(num_dict):
        if num == 0:
            continue
        result += str(i) * num
    return result


if __name__ == '__main__':
    test_cases = int(input())
    for t in range(1, test_cases + 1):
        s = list(input())
        print('Case #{}: {}'.format(t, solve(s)))
