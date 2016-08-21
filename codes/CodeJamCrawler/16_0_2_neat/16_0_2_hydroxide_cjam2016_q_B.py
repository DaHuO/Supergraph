#!/usr/bin/python

import sys

def flipper(stack):
    if '-' not in stack:
        return 0
    elif '+' not in stack:
        return 1
    elif stack[0] == '+':
        return 1 + flipper(stack.lstrip('+'))
    else:
        return 1 + flipper(stack.lstrip('-'))

f = open(sys.argv[1])
o = open(sys.argv[2], 'w')
cases = int(f.readline())
for i in xrange(cases):
    stack = f.readline().strip()
    resul = str(flipper(stack))
    o.write("Case #" + str(i+1) + ': ' + resul + '\n')


o.close()
print "Done, output written"
 
