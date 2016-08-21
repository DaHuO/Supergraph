__author__ = 'snv'

def findmax(s):
    maxdigit = len(s)-1
    for kkk in range(len(s)-1, -1, -1):
        if s[kkk] > s[maxdigit]:
            maxdigit = kkk
    return maxdigit


def lastword(s):
    if len(s) == 0:
        return ''
    k = findmax(s)
    if k + 1 == len(s):
        return s[k] + lastword(s[:k])
    return s[k] + lastword(s[:k])+s[k+1:]



f = open('A-small-attempt0.in','r')
g = open('output.txt', 'w')
n = int(f.readline())
for j in range(n):
    s = f.readline().strip()
    lngth = len(s)
    ans = lastword(s)

    ans_string = 'Case #{0}: {1}\n'.format(j+1, ans)
    print(ans_string)
    g.write(ans_string)
f.close()
g.close()

