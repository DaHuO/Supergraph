from __future__ import print_function
import sys

T = int(sys.stdin.readline())
MAX_TRY = 100
for case in range(T):
    N = int(sys.stdin.readline())
    digits = set()
    
    for i in range(1, MAX_TRY):
        digits |= set(str(i*N))
        if len(digits) == 10:
            break
    print('Case #%d: ' % (case+1,), end='')
    if len(digits) == 10:
        print(i*N)
    else:
        print('INSOMNIA')

