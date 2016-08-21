#!/usr/bin/python3
import sys

def remove_letters(letters, word, ref_letter):
    if (ref_letter in letters and letters[ref_letter] > 0):
        number = letters[ref_letter]
        for ll in word:
            letters[ll] -= number
        return(number)
    else:
        return(0)

def solve_number(SS, case):
    letters = dict()
    for ll in SS:
        if (not ll in letters):
            letters[ll] = 1
        else:
            letters[ll] += 1

    numbers = [0 for ii in range(10)]
    numbers[0] = remove_letters(letters, 'ZERO', 'Z')
    numbers[2] = remove_letters(letters, 'TWO', 'W')
    numbers[8] = remove_letters(letters, 'HEIGHT', 'G')
    numbers[6] = remove_letters(letters, 'SIX', 'X')
    numbers[7] = remove_letters(letters, 'SEVEN', 'S')
    numbers[5] = remove_letters(letters, 'FIVE', 'V')
    numbers[4] = remove_letters(letters, 'FOUR', 'F')
    numbers[9] = remove_letters(letters, 'NINE', 'I')
    numbers[1] = remove_letters(letters, 'ONE', 'N')
    numbers[3] = remove_letters(letters, 'THREE', 'T')

    print("Case #" + str(case) + ": " + ''.join([ str(ii) for ii in range(10) for jj in range(numbers[ii]) ]))


TT = int(input())
for ii in range(TT):
    SS = input()
    solve_number(SS, ii+1)

