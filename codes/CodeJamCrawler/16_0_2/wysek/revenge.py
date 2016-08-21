M = '-'
P = '+'

def solve():
    S = list(input())
    res = 0
    while True:
        lastM = -1
        for si in range(len(S)):
            if S[si] == M:
                lastM = si

        if lastM == -1:
            break

        S = S[:lastM + 1]
        if S[0] == P:
            firstM = 1
            while S[firstM] == P:
                firstM += 1

            for i in range(firstM):
                S[i] = M

            res += 1

        S = list(reversed([M if s == P else P for s in S]))
        res += 1

    return res

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        print ("Case #%d: %s" % (t, solve()))
