from random import *
def tonum(s, p):
    res = 0
    for c in s:
        res = res * p + ord(c) - ord('0')
    return res
T = int(input())
q = []
N, J = map(int, input().split())
print("Case #1:")
for j in range(J):
    s, divs = "", []
    while True:
        s, divs = "1", []
        for i in range(N - 2):
            s += chr(ord('0') + randint(0, 1))
        s += '1'
        if not (s in q):
            gFlag = True
            for p in range(2, 11):
                x = tonum(s, p)
                flag = False
                for d in range(2, 5000):
                    if x % d == 0:
                        flag = True
                        divs.append(d)
                        break
                if not flag:
                    gFlag = False
                    break
            if gFlag:
                q.append(s)
                print(s, end = '')
                for d in divs:
                    print(' ', d, end = '', sep = '')
                print()
                break
            