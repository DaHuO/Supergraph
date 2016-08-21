def m(s):
    if not len(s):
        return 0
    if s[0] == '-':
        return m(s[1:])
    else:
        return 1+p(s[1:])

def p(s):
    if not len(s):
        return 0
    if s[0] == '+':
        return p(s[1:])
    else:
        return 1+m(s[1:])

t = int(input())
for i in range(1,t+1):
    s = input()[::-1]
    n = p(s) if s[0] == '+' else m(s) + 1
        
    print('Case #%d: %d' %(i,n))
