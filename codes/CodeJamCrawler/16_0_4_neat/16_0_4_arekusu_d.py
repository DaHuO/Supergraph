import sys

def findGold(line):
    k, c, s = line.split(" ")
    k, c, s = int(k), int(c), int(s)
    ret = []
    if c > 1:
        kpowc = pow(k, c-1)
        for i in range(1, k+1, 2):
            ii = i if i == k else i+1
            no = (i-1) * kpowc + ii
            ret.append(no)
    else:
        ret = list(range(1, k+1))
    if len(ret) > s:
        return "IMPOSSIBLE"
    else:
        return " ".join([str(x) for x in ret])

if __name__ == "__main__":
    filename = sys.argv[1]
    file = open(filename)
    file.readline()
    i = 0
    for line in file:
        i += 1
        if line.strip() == "":
            continue
        r = findGold(line)
        print "Case #%d: %s" % (i, r)
