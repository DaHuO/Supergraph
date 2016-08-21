import sys

with open(sys.argv[1]) as f:
    content = f.read().splitlines()

with open('io/fractiles.out', 'w') as f:
    T = int(content[0])
    for caseIndex in xrange(1, T+1):
        K, C, S = content[caseIndex].split(' ')
        K = int(K); C = int(C); S = int(S)

        # this will work only for small dataset (as we will not have S = K)
        # checking the first K tiles will work, always for any C !!!
        print 'Case #%d: %s\n' % (caseIndex, ' '.join([str(i) for i in range(1, K+1)]))
        f.write('Case #%d: %s\n' % (caseIndex, ' '.join([str(i) for i in range(1, K+1)])))