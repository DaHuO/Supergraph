#!/usr/bin/python2

LD = {
    "Z": [0],
    "E": [0, 1, 3, 5, 7, 8, 9],
    "R": [0, 3, 4],
    "O": [0, 1, 2, 4],
    "N": [1, 7, 9],
    "T": [2, 3, 8],
    "W": [2],
    "H": [3, 8],
    "F": [4, 5],
    "U": [4],
    "I": [5, 6, 8, 9],
    "V": [5, 7],
    "S": [6, 7],
    "X": [6],
    "G": [8],
}

SD = {
    0: {"Z": 1, "E": 1, "R": 1, "O": 1},
    1: {"O": 1, "N": 1, "E": 1},
    2: {"T": 1, "W": 1, "O": 1},
    3: {"T": 1, "H": 1, "R": 1, "E": 2},
    4: {"F": 1, "O": 1, "U": 1, "R": 1},
    5: {"F": 1, "I": 1, "V": 1, "E": 1},
    6: {"S": 1, "I": 1, "X": 1},
    7: {"S": 1, "E": 2, "V": 1, "N": 1},
    8: {"E": 1, "I": 1, "G": 1, "H": 1, "T": 1},
    9: {"N": 2, "I": 1, "E": 1},
}


def f(S):
    stat = [0] * 26
    for i in S:
        stat[ord(i) - ord("A")] += 1

    ans = []
    for i in [ord(x) - ord("A")
              for x in ["Z", "W", "U", "X", "G", "O", "R", "F", "S", "N"]]:
        ch = chr(i + ord("A"))
        while stat[i] != 0:
            check_list = LD.get(ch)
            for dig in check_list:
                sd = SD[dig]
                ok = True
                for d, c in sd.iteritems():
                    idx = ord(d) - ord("A")
                    if stat[idx] < c:
                        ok = False
                        break
                if ok:
                    ans.append(dig)
                    for d, c in sd.iteritems():
                        idx = ord(d) - ord("A")
                        stat[idx] -= c
                    break
    return "".join([str(x) for x in sorted(ans)])


import sys
fd = open(sys.argv[1], "rb")
T = int(fd.readline().strip())
for i in xrange(1, T + 1):
    s = fd.readline().strip()
    res = f(s)
    print "Case #%d: %s" % (i, res)
fd.close()
