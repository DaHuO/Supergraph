#!/usr/bin/python
import sys
for i in range(1, int(raw_input())+1):
    num = int(raw_input())
    if num == 0:
        print "Case #{}: INSOMNIA".format(i)
        continue
    s = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    for n in range(1,75):
        s -= (set(list(str(num*n))))
        if len(s) == 0:
            break
    print "Case #{}:".format(i), num*n
sys.exit()
