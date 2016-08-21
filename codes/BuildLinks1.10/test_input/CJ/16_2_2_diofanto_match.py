def match(s1, s2, m1, m2):
    if '?' in s1:
        idx = s1.index('?')
        for d in '0123456789':
            s1[idx] = d
            m1, m2 = match(s1[:], s2[:], m1, m2)
    elif '?' in s2:
        idx = s2.index('?')
        for d in '0123456789':
            s2[idx] = d
            m1, m2 = match(s1[:], s2[:], m1, m2)
    else:
        n1 = int(''.join(s1))
        n2 = int(''.join(s2))
        d = abs(n1 - n2)
        d1 = abs(m1-m2)
        if m1 == -1 or d < d1:
            return (n1,n2)
        elif d == d1:
            if n1 < m1:
                return (n1,n2)
            elif n1 == m1:
                if n2 < m2:
                    return (n1,n2)
                else:
                    return (m1,m2)
            else:
                return (m1,m2)
        else:
            return (m1,m2)
    return m1, m2

def pad(n1, n2, l):
    n1 = str(n1)
    n2 = str(n2)
    p1 = ''.join(["0" for _ in range(l - len(n1))])
    p2 = ''.join(["0" for _ in range(l - len(n2))])
    return p1+n1, p2+n2


for t in range(1, int(input())+1):
    s1, s2 = input().split()
    l = len(s1)
    s1 = [c for c in s1]
    s2 = [c for c in s2]
    n1, n2 = match(s1, s2, -1, -1)
    n1, n2 = pad(n1, n2, l)
    print("Case #{0}: {1}".format(t, n1 + " " + n2))
