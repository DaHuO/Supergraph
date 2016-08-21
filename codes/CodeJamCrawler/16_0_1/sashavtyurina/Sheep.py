import sys

filename = sys.argv[1]

f = open(filename)
cases = int(f.readline())


for case in range(0, cases):
    N = int(f.readline().strip())

    if (N == 0):
        print('Case #%d: INSOMNIA' % (case+1))
        continue
    
    i = 1
    allDigits = set([str(d) for d in  range(10)])
    while allDigits:
        allDigits.difference_update(set(str(N*i)))
        i += 1

    print('Case #%d: %d' % (case+1, N * (i-1)) )