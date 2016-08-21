import sys

__author__ = 'PC'

def output(out, tc, res):
    out.write("Case #%s: %s\n" % (tc, res))

with open('output', 'w+') as out:
    with open(sys.argv[1], 'r') as f:
        T = int(f.readline())
        for tc in range(1, T + 1):
            N = int(f.readline())

            if N == 0:
                output(out, tc, "INSOMNIA")
            else:
                count = 1
                numbers = [str(x) for x in range(10)]
                while True:
                    S = str(count * N)
                    numbers = list(filter(lambda x: x not in S, numbers))
                    if not numbers:
                        output(out, tc, S)
                        break
                    count += 1



