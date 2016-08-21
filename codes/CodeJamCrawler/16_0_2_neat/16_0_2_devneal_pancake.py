#!/usr/bin/python

T = input()

for i in range(1,T+1):
    line = raw_input()

    if line[0] == "-":
        ans = 1
        if line.find("+") != -1:
            line = line[line.find("+"):]
        else:
            line = ""
    else:
        ans = 0

    while line and line.find("-") != -1:
        # find start of '-' chars
        line = line[line.find("-"):]
        # find start of next '+' chars (if any)
        if line.find("+") != -1:
            line = line[line.find("+"):]
        else:
            line = ""
        ans += 2

    print "Case #{}: {}".format(i, ans)
