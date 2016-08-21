def chplus (s):
    c = 0
    for i in reversed(s):
        if i == '+' : c+=1
        else : break
    return s[:len(s)-c]

def countplus (s):
    c = 0
    for i in s:
        if i == '+' : c+=1
        else : break
    return c

def flip (s,n ):
    for i in range(n): s[i] = '-' if s[i] == '+' else '+'
    return "".join(list(reversed(s[:n])) + s[n:])

t = int(input().strip())
for case in range(t):
    s = chplus(input().strip())
    c =0 
    while len(s)>0 :
        c+=1
        cs = countplus(s)
        if cs > 0 :
            s=flip(list(s),cs)
        else : s=flip(list(s),len(s))
        s = chplus(s)
    print("Case #%d:" % (case+1),c)   