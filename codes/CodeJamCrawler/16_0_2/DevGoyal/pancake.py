import numpy as np
import sys

def count_num_flips(line):
    """
    Keyword Arguments:
    line -- 
    """
    iterable = (c == '+' for c in line[:-1])
    signs = np.fromiter(iterable, np.bool, len(line)-1)

    count = 0
    for i in range(len(signs)-1):
        count = count + (signs[i] != signs[i+1])
    count = count + (not signs[-1])

    return count

def main():
    """
    
    """
    N = int(next(sys.stdin))
    for i in range(1, N+1):
        sys.stdout.write('Case #{:d}: {}\n'.format(i, count_num_flips(next(sys.stdin))))
        

if __name__=='__main__':
    main()
