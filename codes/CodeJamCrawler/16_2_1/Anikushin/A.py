import sys

with open("out.txt", "w") as fout:
    with open("A.in", "r") as f:
      n = int(f.readline())
      for i in xrange(n):
        s = f.readline()
        r = [0] * 10
        a = {}
        for c in s+"ZXWUGROSFI":
            a[c] = 0
        for c in s:
            a[c] = a[c] + 1
        while a['Z'] > 0:
            r[0] += 1
            for c in "ZERO":
                a[c] -= 1
        while a['X'] > 0:
            r[6] += 1
            for c in "SIX":
                a[c] -= 1
        while a['W'] > 0:
            r[2] += 1
            for c in "TWO":
                a[c] -= 1
        while a['U'] > 0:
            r[4] += 1
            for c in "FOUR":
                a[c] -= 1
        while a['G'] > 0:
            r[8] += 1
            for c in "EIGHT":
                a[c] -= 1
        while a['R'] > 0:
            r[3] += 1
            for c in "THREE":
                a[c] -= 1
        while a['O'] > 0:
            r[1] += 1
            for c in "ONE":
                a[c] -= 1
        while a['S'] > 0:
            r[7] += 1
            for c in "SEVEN":
                a[c] -= 1
        while a['F'] > 0:
            r[5] += 1
            for c in "FIVE":
                a[c] -= 1
        while a['I'] > 0:
            r[9] += 1
            for c in "NINE":
                a[c] -= 1
        res = "".join(map(lambda x: str(x[0])*x[1], enumerate(r)))
        fout.write("case #%d: %s\n" % (i+1, res))
