from sys import stdin

def firstdivisor(a):
    for x in range(2, int(a ** 0.5) + 1):
        if a % x == 0:
            return x

def solve(N):
    for i in range(1, 2**(N-2)):
        s = ("1{0:0%sb}1" % (N-2)).format(65535*i)
        if len(s) != N:
            continue
        flag = True
        lst = []
        for b in range(2, 10+1):
            r = firstdivisor(int(s, b))

            if r == None:
                flag = False

            lst.append(r)
        if flag:
            yield "%s %s" % (s, " ".join(map(str, lst)))

T = 1
N, J = 32, 500

print("Case #1:")
for _, b in zip(range(J), solve(N)):
    print(b)
