

import sys





def solve(N):
    if N == 0:
        return "INSOMNIA"

    cnt = 0
    flags = [-1] * 10

    res = 0
    i = 1
    while cnt < 10:
        # count
        tmp = N * i
        res = tmp
        while tmp > 0:
            idx = tmp % 10
            tmp /= 10
            cnt += int(flags[idx] == -1)
            flags[idx] = 1

        i += 1

    return str(res)        


def main():
    T = int(sys.stdin.readline().strip())
    for t in range(T):
        N = int(sys.stdin.readline().strip())
        print "Case #%d: %s" % (t+1, solve(N))




main()
