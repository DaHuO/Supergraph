import sys

def countingSheep(x):
    if (x == 0):
        return "INSOMNIA"
    allSet = set("0123456789")
    count = 0
    curr = 0
    while (allSet):
        count += 1
        curr += x
        allSet -= set(str(curr))
    # print x, count, curr
    return curr

n = int(raw_input())
for i in range(n):
    t = int(raw_input())
    print "Case #{}: {}".format(i + 1, countingSheep(t))
