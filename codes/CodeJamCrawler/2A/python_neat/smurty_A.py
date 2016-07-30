
let = 'RPS'

def cons(a, n):
    if n == 0: return let[max(range(3),key=lambda i: a[i])]
    ww = [0]*3
    bw = [0]*3
    gotmore = False
    for i in xrange(3):
        if a[i] % 2 == 1:
            if gotmore: ww[i] = a[i] // 2
            else:
                ww[i] = a[i] // 2 + 1
                gotmore = True
        else:
            ww[i] = a[i] / 2
        bw[i] = a[i]-ww[i]
    x = cons(ww, n-1)
    y = cons(bw, n-1)
    if x < y:return x+y
    else:return y+x
            
T = input()
for c in xrange(1, T+1):
    print 'Case #%d:' % c,
    n, r, p, s = map(int, raw_input().split())
    good = {2**n//3, 2**n//3 + 1}
    if r in good and p in good and s in good:
        print cons([r,p,s],n)
    else:
        print 'IMPOSSIBLE'
    



    
