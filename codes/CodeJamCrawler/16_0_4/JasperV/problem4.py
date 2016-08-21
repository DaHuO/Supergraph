import math
def findSolution2(k, c, s):
    if s < k:
        return "IMPOSSIBLE"
    else:
        return " ".join(map(str, list(range(0, k))))

def findSolution(k, c, s):
    if s < k:
        print("lol")
    if s == 0 or (k != 1 and c != 1 and s < k-1) or (c == 1 and s < k):
        return "IMPOSSIBLE"
    elif k == 1:
        return "1"
    else:
        if c > 1:
            return " ".join(map(str, list(range(2, k+1))))
        else:
            return " ".join(map(str, list(range(1, k+1))))
            
inp = open("D-small-attempt5.in", "r")
res = open("out1.txt", "w")
cases = int(inp.readline())
lines = []
for i in range(cases):
    lines.append(map(int,inp.readline().split()))
for i in range(len(lines)):
    res.write("Case #" + str(i+1) + ": " + findSolution(*lines[i]) + "\n")
    print(i)