import numpy as np
import sys

def process_line(line):
    """
    Keyword Arguments:
    line -- 
    """
    k, c, s = [int(c) for c in line.split()]

    indices = []
    span = k**(c-1)
    for i in range(1, k+1):
        indices.append(span*i)
    return indices

def main():
    """
    
    """
    N = int(next(sys.stdin))
    for i in range(1, N+1):
        sys.stdout.write('Case #{:d}: {}\n'.format(i, ' '.join(map(str, process_line(next(sys.stdin))))))

if __name__=='__main__':
    main()
