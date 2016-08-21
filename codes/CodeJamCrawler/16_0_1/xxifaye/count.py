import math
import sys

def solve():
    num = int(sys.stdin.readline())

    if num == 0:
        return 'INSOMNIA'
    unseen = set(map(str, xrange(10)))
    n = num
    while len(unseen) > 0:
        t = str(n)
        for i in unseen.copy():
            if i in t:
                unseen.remove(i)
        n += num
    return  n-num


if __name__ == '__main__':
    n = sys.stdin.readline()
    for i in xrange(int(n)):
        print "Case #{}: {}".format(i+1, solve())
        sys.stdout.flush()


