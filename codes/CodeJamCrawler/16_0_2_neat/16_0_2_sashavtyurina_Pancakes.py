import sys

filename = sys.argv[1]

f = open(filename)
cases = int(f.readline())


for case in range(0, cases):
    inputSeq = f.readline().strip()

    transitions = inputSeq.count('-+')
    transitions += inputSeq.count('+-')
    if inputSeq[-1] == '-':
        transitions += 1
    
    print('Case #%d: %d' % (case + 1, transitions))


