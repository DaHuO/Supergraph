import math


def solve():
    f = open("B-large.in", "r")
    T = int(f.readline())
    out = open("output.txt", "w")

    for case in range(T):
        S = f.readline().strip()
        sn = [0 if i == '-' else 1 for i in S]
        r = len(sn)
        while r - 1 >= 0 and sn[r - 1] == 1:
            r -= 1
        count = 0

        while r > 0:
            sel = 0
            while sel + 1 < r and sn[sel] == sn[sel + 1]:
                sel += 1
            if sn[0] == 1:
                count += 1
                for i in range(sel + 1):
                    sn[i] = 0
                while sel + 1 < r and sn[sel + 1] == 0:
                    sel += 1

            count += 1
            for i in range(math.ceil(r / 2)):
                t = sn[i]
                sn[i] = 1 - sn[r - i - 1]
                sn[r - i - 1] = 1 - t
                if i == r - i - 1:
                    break
            while r - 1 >= 0 and sn[r - 1] == 1:
                r -= 1
        print("Case #%d: %d" % (case + 1, count))
        out.write("Case #%d: %d\n" % (case + 1, count))


solve()
