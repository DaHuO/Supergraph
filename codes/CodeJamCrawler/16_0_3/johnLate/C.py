#!/usr/bin/env pypy3


def testcase(tc, N, J, prime):
    print("Case #{}:".format(tc))

    j = 1
    for i in range(1<<(N-2)):
        string = '1' + '{:0{}b}'.format(i, N-2) + '1'
        res = []

        for b in range(2, 11):
            num = int(string, b)
            fount = False
            for d in prime:
                if d*d > num: break
                if num % d == 0:
                    found = True
                    res.append(d)
                    break
            if not found:
                break
        if len(res) == 9:
            print(string, ' '.join([str(x) for x in res]))
            j += 1
            if j > J: break

def main():
    prime = []
    nonprime = [False for _ in range(1<<17)]
    nonprime[0] = nonprime[1] = True
    for k in range(2, 1<<17):
        if not nonprime[k]:
            prime.append(k)
            for x in range(k+k, 1<<17, k):
                nonprime[x] = True

    TC = int(input())
    for tc in range(1, TC+1):
        N, J = [int(x) for x in input().split(' ')]
        testcase(tc, N, J, prime)


if __name__ == '__main__':
    main()
