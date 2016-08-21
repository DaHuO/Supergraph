import fileinput
import sys

N = int(sys.stdin.readline())

for lineNum in range(N):
    n = int(sys.stdin.readline())

    print 'case #{0}:'.format(lineNum+1),

    i = 1
    s = set()
    while True:
        if i > 1000000:
            print 'INSOMNIA'
            break
        
        for a in str(i*n):
            if a not in s:
                s.add(a)

        if len(s) >= 10:
            print i*n
            break

        i += 1
