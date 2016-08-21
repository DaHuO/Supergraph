
import sys


def verify(k):
    b = [False for i in range(10)]
    done = 0
    r = 0
    while done < 10:
        r = r + k
        t = r
        while t:
            if not b[t % 10]:
                b[t % 10] = True
                done = done + 1
            t = int(t / 10)
    return r

sys.stdin.readline()
for i, w in enumerate(sys.stdin.readlines()):
    w = int(w.strip())
    if w == 0:
        print("Case #%d: INSOMNIA" % (i + 1))
    else:
        print("Case #%s: %s" % (i + 1, verify(int(w))))
