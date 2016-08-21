import numpy as np
from time import time

def solve_small(length, complexity, tiles):
    ''' Assumes lenght == tiles'''
#    assert length==tiles, 'length!=tiles'
    if length!=tiles:
        return None
    sol = []
    k = length**(complexity-1)
    for i in range(length) :
        sol.append(k * i + 1)
    return sol
        
    
if __name__ == '__main__' :
    
    fileName = 'D-small-attempt1'
    with open(fileName + '.in', 'r') as f, \
         open(fileName + '.out', 'w') as fout:
        start = time()
        
        n_cases = int(f.readline()) 
        for i in range(1, n_cases+1) :
            # Read a case
            length, complexity, tiles = [int(x) for x in f.readline().split()]
            
            # Solve and print            
            solution = solve_small(length, complexity, tiles)

            output = 'Case #%d:' % (i,)
            print(length, complexity, tiles)
            print(output)
            fout.write(output)
            
            if solution == None:
                fout.write(' IMPOSSIBLE\n')
                print('IMPOSSIBLE')
            else:
                for tile in solution:
                    fout.write(' %d' % tile)
                fout.write('\n')
                print(solution)
            print('\n')


        elapsed = time() - start
        print('Elapsed time: %g' % elapsed)
            
