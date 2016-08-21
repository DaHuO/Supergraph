#! /usr/bin/python

import sys

filter = [
    ['W', "TWO", '2'],
    ['X', "SIX", '6'],
    ['G', "EIGHT", '8'],
    ['Z', "ZERO", '0'],
    ['U', "FOUR", '4'],
    ['R', "THREE", '3'],
    ['O', "ONE", '1'],
    ['F', "FIVE", '5'],
    ['V', "SEVEN", '7'],
    ['N', "NINE", '9'],
]


if __name__ == "__main__":
    num_tests = int(sys.stdin.readline())
    
    for test_number in range(1, num_tests + 1):
        clue = sys.stdin.readline().strip()
        phone_number = ""
        
        for criterion, letters, digit in filter:
            while clue.find(criterion) > -1:
                # remove letters from clue
                for letter in letters:
                    clue = clue.replace(letter, '', 1)
                # add digit to phone number 
                phone_number += digit
                
        print "Case #{}: {}".format(test_number, "".join(sorted(phone_number)))