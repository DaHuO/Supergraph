#!/usr/bin/env python

def flippy(line):
    # if bottom pancake is then we flip everything above,
    # then recursively call flippy on the next pancake up
    if(len(line) == 0):
        return 0
    
    if(line[len(line)-1] == "-"):
        line = flip(line)
        return 1 + flippy(line[0:len(line)-1])
    else:
        return flippy(line[0:len(line)-1])


def flip(line):
    result = ""
    for c in line:
        if(c=="+"):
            result += "-"
        else:
            result += "+"
            
    return result


# MAIN METHOD STARTS HERE.

n = int(raw_input())

printlist = []

for i in range(n):
    line = raw_input().strip()
    x = flippy(line)
    printlist.append("Case #{}: {}".format(i+1, x))

for i in range(len(printlist)):
    print(printlist[i])




