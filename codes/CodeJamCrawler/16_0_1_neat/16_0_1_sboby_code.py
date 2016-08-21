import numpy as np
from time import time

def count_sheeps(n, verbose=False):
    if n == 0:
        return 'INSOMNIA'
    to_found = set(range(10))       # digits to found
    count = 0
    while len(to_found) > 0:        
        count += n
        if verbose:
            print(count)
        digits = [int(d) for d in str(count)]
        for d in digits:
            to_found.discard(d)
    return count
        
    
if __name__ == '__main__' :
    fileName = 'A-large'
    with open(fileName + '.in', 'r') as f, \
         open(fileName + '.out', 'w') as fout:
        start = time()
        
        n_cases = int(f.readline()) 
        for i in range(1, n_cases+1) :
            # Read a case
            N = int(f.readline())
            
            # Solve and print
            solution = count_sheeps(N)
            output = 'Case #%d: %s\n' % (i, str(solution))
            fout.write(output)
            print(output)

        elapsed = time() - start
        print('Elapsed time: %g' % elapsed)
            
