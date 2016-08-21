import sys

# sys.setrecursionlimit(20)

besta, bestb, mindif = 0, 0, 0

m0 = lambda d: '0' if d == '?' else d
m9 = lambda d: '9' if d == '?' else d
 
mini = lambda x: int("".join(map(m0, x)))
maxi = lambda x: int("".join(map(m9, x)))

def solve():
    global besta, bestb, mindif
    
    a, b = map(list, input().split())
    besta, bestb = mini(a), mini(b)
    mindif = abs(besta-bestb)

    def better(na, nb):
        global besta, bestb, mindif
        if abs(na-nb) < mindif:
            besta, bestb, mindif = na, nb, abs(na-nb)

    def try_pos(i, filla=None, fillb=None):
        if (filla is not None and (filla < 0 or filla > 9)) or (fillb is not None and (fillb < 0 or fillb > 9)):
            return

        if i >= len(a):
            better(mini(a), mini(b))
            return

        olda, oldb = a[i], b[i]
        if filla is not None:
            a[i] = str(filla)
        if fillb is not None:
            b[i] = str(fillb)
                
        if a[i] == '?' and b[i] == '?':
            try_pos(i, 0, 0)
            try_pos(i, 0, 1)
            try_pos(i, 1, 0)
        
        elif a[i] == '?':
            bb = int(b[i])
            try_pos(i, bb-1, bb)
            try_pos(i, bb, bb)
            try_pos(i, bb+1, bb)

        elif b[i] == '?':
            aa = int(a[i])
            try_pos(i, aa, aa-1)
            try_pos(i, aa, aa)
            try_pos(i, aa, aa+1)
            
        else:
            if a[i] == b[i]:
                try_pos(i+1)
            elif a[i] > b[i]:
                better(mini(a), maxi(b))
            else:
                better(maxi(a), mini(b))

        a[i], b[i] = olda, oldb

    try_pos(0)
    return " ".join(map(lambda x: str(x).zfill(len(a)), [besta, bestb]))

T = int(input())

for t in range(T):
    ans = solve()
    print("Case #{}: {}".format(t+1, ans)) 