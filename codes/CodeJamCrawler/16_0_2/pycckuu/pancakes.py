# from __future__ import print_function
import fileinput
import re

with open('B-large.in', 'r') as f:
    lines = f.read().splitlines()

f1 = open('output', 'w+')

n = int(lines[0])


for j in xrange(1, n + 1):
    # print lines[j].count('-')
    p = re.compile('[-]+')
    counter =  2*len(p.findall(lines[j]))
    if lines[j][0] == '-': counter-=1
    f1.write("Case #%i: %s\n" % (j, counter))
    print ("Case #%i: %s" % (j, counter))
