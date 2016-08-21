#Joe Snider
#4/16
#
#code jam 2016, qual A

#n is the number to digitify and add, total is a dict
#total has length 10 means success (return true)
def update(n, total):
    #strings are fast enough (test up to 10^6 in a few secs)
    for c in str(n):
        total[int(c)] = 1
    return len(total)==10

import sys
sys.stdin.readline()
count = 0
for line in sys.stdin:
    i = int(line)
#for i in range(100000):
    count += 1
    j = 1
    total = {}
    while not update(j*i, total) and j < 1000:
        j += 1
    if j == 1000:
        print "Case #%d: INSOMNIA"%(count)
    else:
        print "Case #%d: %d"%(count, i*j)
