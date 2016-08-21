#!usr/bin/python
import sys

def solve(testcase):
    print "Case #%d:" % testcase,
    i = int(sys.stdin.readline().strip())
    used = set()
    if not i:
        print "INSOMNIA"
        return
    j = 1
    while True:
        used |= set(str(j*i))
        if len(used) == 10:
            print j*i
            return
        j += 1

t = int(sys.stdin.readline().strip())
for case in range(t):
    solve(case+1)


