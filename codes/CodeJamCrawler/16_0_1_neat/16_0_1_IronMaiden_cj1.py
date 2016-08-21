
import sys
sys.stdout = open('out.txt', 'w')


def finish(dig):
    flag = 1
    for x in dig:
        if x == 0:
            flag = 0
    return flag


with open('in.txt') as f:
    t = int(next(f))
    for cnt in range(1, t + 1):
        dig = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        n = int(next(f))
        ori = n
        ii = 2
        if n is 0:
            print("Case #" + str(cnt) + ": INSOMNIA")
            continue
        while finish(dig) is 0:

            digits = [int(i) for i in str(n)]

            for x in digits:

                dig[x] = 1

            if finish(dig):
                print("Case #" + str(cnt) + ": " + str(n))
                continue
            else:
                n = ori * ii
                ii = ii + 1
        t = t - 1
