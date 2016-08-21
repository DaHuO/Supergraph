
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
instances = []
for i in xrange(1, t + 1):
    instances.append((raw_input()))


import re

pton = re.compile("\+-")
ntop = re.compile("-\+")

#instances = ['+++++-------','+-+-+-+-+-+-']
for i in range(1,t+1):
    if instances[i-1]:
        start = 0 if instances[i-1][-1] == '+' else 1
    else:
        start = 0
    postoneg = len(pton.findall(instances[i-1]))
    negtopos = len(ntop.findall(instances[i-1]))
    #print postoneg, negtopos, start
    print 'Case #' + str(i) + ': ',postoneg + negtopos + start