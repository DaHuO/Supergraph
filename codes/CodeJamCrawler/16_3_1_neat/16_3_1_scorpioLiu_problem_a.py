import sys

# sys.stdin = open('A-small-attempt0.in', 'r')
sys.stdin = open('A-large.in', 'r')
# sys.stdout = open('a-small.out', 'w')
sys.stdout = open('a-large.out', 'w')

def check(s):
    t = 0
    for i in s:
        t += i[1]
    if t == 0:
        return False
    for i in s:
        if i[1] * 1.0 / t > 0.5:
            return True
    return False

def solution(n, p):
    a = 'A'
    s = []
    for i, v in enumerate(p):
        s.append([chr(ord(a) + i), v])
    t = 0
    for i in s:
        t += i[1]
    res = []
    while t > 0:
        hit = False
        for i in range(n):
            if s[i][1] < 1:
                continue
            for j in range(i, n):
                s[i][1] -= 1
                if s[j][1] < 1:
                    s[i][1] += 1
                    continue
                s[j][1] -= 1
                if not check(s):
                    res.append(s[i][0] + s[j][0])
                    t -= 2
                    hit = True
                    break
                else:
                    s[i][1] += 1
                    s[j][1] += 1
            if hit:
                break
        if hit:
            continue
        for i in range(n):
            if s[i][1] < 1:
                continue
            s[i][1] -= 1
            if not check(s):
                hit = True
                t -= 1
                res.append(s[i][0])
            else:
                s[i][1] += 1
    return ' '.join(res)

for t in range(int(input())):
    n = int(raw_input())
    p = [int(i) for i in raw_input().split()]
    r = solution(n, p)
    print 'Case #%d: %s' % (t + 1, r)
