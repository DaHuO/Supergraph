alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def proc(lst):
    l = []
    c = sum(lst)
    while c > 0:
        m = max(lst)
        a = lst.index(m)
        lst[a] -= 1
        if c > 3:
            try:
                b = lst.index(m)
                lst[b] -= 1
                l += [alph[a] + alph[b]]
                c -= 2
            except:
                l += [alph[a]]
                c -= 1
        elif c == 3:
            l += [alph[a]]
            c -= 1
        else:
            l += [alph[a] + alph[lst.index(max(lst))]]
            c -= 2
    return l

T = int(raw_input())
for i in xrange(T):
    N = int(raw_input())
    A = [int(x) for x in raw_input().split()]
    print 'Case #%d: ' % (i+1) + ' '.join(proc(A))
