from collections import deque
def solve(s,k):
    d=deque(s[0])
    for i in s[1:]:
        if d[0]<=i:
            d.appendleft(i)
        else:
            d.append(i)
    temp=''.join(d)
    print 'Case #'+str(k+1)+': '+temp



    

n=int(raw_input())
for i in range(n):
    s=raw_input()
    solve(s,i)

