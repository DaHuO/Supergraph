import sys

def removerepeats(s):
    resstr = ""

    #empty string
    if len(s) == 0:
        return s

    cur = s[0]
    resstr = cur
    for i in range(1, len(s)):
        if s[i] != cur:
            resstr = resstr + s[i]
            cur = s[i]

    return resstr

def numflips(s):
    #first, parse and remove all repeats
    s = removerepeats(s)

    #at least one needed to flip
    if len(s) < 1:
        return 0

    cur = s[0]
    ndiff = 0
    for i in range(1, len(s)):
        #if different, we increment
        if s[i] != cur:
            ndiff = ndiff + 1
            cur = s[i]

    #last is minus, final flip
    if len(s) >= 1 and s[len(s) - 1] == "-":
        ndiff = ndiff + 1

    return ndiff;


def main():
    #print("reading " + sys.argv[1])
    f = open(sys.argv[1])

    t = int(f.readline())

    for i in range(1, t+1):
        s = f.readline().split()[0]
        flips = numflips(s)
        print("Case #" + str(i) + ": " + str(flips))

main()
