import queue

FILE = open('a.in', 'r')
out = open('o.out', 'w')
FILE.readline()

def isAllUp(stack):
    for pancake in stack[0]:
        if (pancake == "-"):
            return False
    return True

def flipStr(n, s):
    toflip = s[0:n]
    toflip = toflip[::-1]
    flipped = ''
    for x in toflip:
        if (x == "+"):
            flipped += "-"
        else:
            flipped += "+"
    return flipped + s[n:]

def solve(stack):
    q = queue.Queue()
    q.put(stack)
    sofar = {stack[0]}
    while (not q.empty()):
        cur = q.get()
        sofar.add(cur[0])
        if (isAllUp(cur)):
            return cur[1]
        for i in range(1, len(cur[0])):
            newstr = flipStr(i, cur[0])
            if (newstr not in sofar):
                q.put([newstr, cur[1] + 1])

i = 1
for line in FILE:
    out.write("Case #" + str(i) + ": " + str(solve([line, 0])) + "\n")
    i += 1
