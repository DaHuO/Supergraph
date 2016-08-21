import numpy as np
import os
from time import time

from string import ascii_uppercase
#digits = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
#l2d = {i: set() for i in ascii_uppercase}
#for value, string in enumerate(digits):
#    for letter in string:
#        l2d[letter].add(value)
        
digit2str = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']

# For every letter, find the digits containing that letter
l2d = {} # letter to digits
for value, string in enumerate(digit2str):
    for letter in string:
        if letter not in l2d:
            l2d[letter] = set()
        l2d[letter].add(value)

levels = []
for i in range(3):  
    n_digits = {letter: len(digits) for letter, digits in l2d.items()}
    one_choice = {letter: digit.pop() for letter, digit in l2d.items() if n_digits[letter]==1}
    levels.append(one_choice)
    for letter, digit in one_choice.items():
        del l2d[letter]
        for digit_set in l2d.values():
            digit_set.discard(digit) 


def count(s):
    ''' Counts the number of occurrences of letters in a string '''
    d = {letter: 0 for letter in ascii_uppercase}
    for letter in s:
        d[letter] += 1
    return d

def solve(s):
    global levels, digit2str
    sol = []
    len_s = len(s)
    counts = count(s)
    for level in levels:
        for letter, digit in level.items():
            if counts[letter] > 0:
                digit_str = digit2str[digit]
                c = counts[letter]
                for j in range(c):
                    sol.append(digit)
                for l in digit_str:
                    counts[l] -= c
                len_s -= c * len(digit_str)
                
                if len_s == 0:
                    break
        if len_s == 0:
            break
    
    assert len_s==0, "Something didn't work!"
    sol.sort()
    return ''.join(map(str, sol))


## Test
#for i in range(100) :
#    seq = np.random.randint(0, 10, 20)
#    seq.sort()
#    f = lambda i: digit2str[i] 
#    string = ''.join(map(f, seq))
#    sol = ''.join(map(str, seq))
#    out = solve(string)
#    assert sol==out, 'Output: %s\n Correct: %s' % (out, sol)
    
        
if __name__ == '__main__' :
    file_name = 'A-large'
    input_path = os.path.join('input', file_name + '.in') 
    output_path = os.path.join('output', file_name + '.out')
    with open(input_path, 'r') as f, \
         open(output_path, 'w') as fout:
        start = time()
        
        n_cases = int(f.readline()) 
        for i in range(1, n_cases+1) :
            # Read a case
            string = f.readline().strip()
            
            # Solve and print  
            output = 'Case #%d: %s\n' % (i, solve(string))
            fout.write(output)
            print(output)

        elapsed = time() - start
        print('Elapsed time: %g' % elapsed)
            
