def flatten(inp):
    if inp == "":
        return ""
    res = inp[0]
    current = inp[0]
    for i in inp:
        if i != current:
            current = i
            res += i
    print(res)
    return res
    
def removeFinished(inp):
    for i in range(len(inp) - 1, -1, -1):
        if inp[i] == "-":
            return inp[:i+1]
    return ""

def flip(inp, end):
    res = ""
    for i in range(end - 1, -1, -1):
        if inp[i] == "+":
            res += "-"
        else:
            res += "+"
    return res + inp[end:]
    
def findSolution(inp):
    remaining = inp
    remaining = removeFinished(remaining)
    remaining = flatten(remaining)
    return str(len(remaining))
    
inp = open("B-large.in", "r")
res = open("out1.txt", "w")
cases = int(inp.readline())
lines = []
for i in range(cases):
    lines.append(inp.readline())
for i in range(cases):
    res.write("Case #" + str(i+1) + ": " + findSolution(lines[i]) + "\n")
    print(i)