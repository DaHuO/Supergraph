import sys

T=int(sys.stdin.readline().strip())

for k in range(1, T + 1):
    N = int(sys.stdin.readline().strip())

    j = 1
    p = str(N * j)

    if p == '0':
        print("Case #%d: INSOMNIA" % k)
    else:
        num = set()
        while True:
            for c in p:
                num.add(c)

            if len(num) == 10:
                print("Case #%d: %s" % (k, p))
                break
            else:
                j += 1
                p = str(N * j)
                

