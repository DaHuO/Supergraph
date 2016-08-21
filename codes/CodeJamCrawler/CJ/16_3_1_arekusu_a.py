import sys

def func(arr):
    arr = [int(x) for x in arr]
    parties = []
    for i, a in enumerate(arr):
        name = chr(i+ord("A"))
        parties.append([a, name])
    parties = sorted(parties, reverse=True)
    ret = []
    while len(parties) != 0:
        if len(parties) == 3 and parties[0][0] == 1:
            ret.append(parties[0][1])
            parties[0][0] -= 1
        elif len(parties) >= 2:
            ret.append(parties[0][1] + parties[1][1])
            parties[0][0] -= 1
            parties[1][0] -= 1
        else:
            ret.append(parties[0][1])
            parties[0][0] -= 1
        parties = sorted([x for x in parties if x[0] != 0], reverse=True)

    return ret

if __name__ == "__main__":
    filename = "/Users/arekusuri/data.txt"
    file = open(filename)
    n = int(file.readline().strip())

    for i in range(n):
        line = file.readline()
        arr = file.readline().strip().split()
        r = func(arr)
        r = " ".join(r)
        print "Case #%d: %s" % (i+1, r)
