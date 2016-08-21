#!/usr/bin/python
input = open("B-large.in")
T = int(input.readline())
for t in range(T):
    start = list(input.readline().strip())
    ans = 0
    while True:
        if "-" not in start:
            print "Case #%s: %s" % (t+1, ans)
            break
        ans = ans+1
        if start[0] == "-":
            if "+" in start:
                idx = start.index("+")
            else:
                idx = len(start)
            for i in range(idx):
                start[i] = "+"
        else:
            if "-" in start:
                idx = start.index("-")
            else:
                idx = len(start)
            for i in range(idx):
                start[i] = "-"
     
    
