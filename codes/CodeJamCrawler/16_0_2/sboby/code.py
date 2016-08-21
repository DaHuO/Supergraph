#import numpy as np
from time import time


def first_index(value, x, from_end=False):
    '''
    Return the index of the first element with the specified value. If from_end
    is setted to true, return the index of the first element, starting from the
    end. Even in this case, the returned index is 
    '''
    length = len(x)
    if from_end:
        x = reversed(x)
    for i, v in enumerate(x):
        if v == value:
            return (length - i - 1) if from_end else i
    return -1

    
def flip(stack):
    flipped = lambda x: '+' if x=='-' else '-'
    stack[:] = [flipped(pancake) for pancake in reversed(stack)]
    return stack


def solve(stack_string):
    s = [c for c in stack_string]
    n_flips = 0
    # remove all +'s at the bottom
    new_end = first_index('-', s, from_end=True) + 1
    s = s[:new_end]
    while len(s) > 0:
        # if at the top there are a sequence of '+', we need to flip them first
        # to flip the entire stack
        first_minus = first_index('-', s)
        if first_minus != 0:
            # here, imagine to flip s[:first_minus] (in this implementation 
            # it's superfluos to do it). Instead we can increment n_flips and
            # remove all these '+' at the top, because them will be removed
            # after flipping the entire stack.
            n_flips += 1
            s = s[first_minus:]
            
        # remove all the '-' at the top: after flipping the entire stack, 
        # these minus will be '+' at the bottom.
        first_plus = first_index('+', s)
        if first_plus < 0:
            s = []   # no more '+': s is a stack of '-'; we've done
        else:
            s = s[first_plus:]
            s[:] = flip(s)
        n_flips += 1
        
    return n_flips


if __name__ == '__main__' :
    
    fileName = 'B-large'
    with open(fileName + '.in', 'r') as f, \
         open(fileName + '.out', 'w') as fout:
        start = time()
        
        n_cases = int(f.readline()) 
        for i in range(1, n_cases+1) :
            # Read a case
            stack = f.readline().strip()
            print(stack)
            # Solve and print
            sol = solve(stack)
            output = 'Case #%d: %d\n' % (i, sol)
            fout.write(output)
            print(output)
            
        elapsed = time() - start
        print('Elapsed time: %g' % elapsed)
            
