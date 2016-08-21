import sys
t = int(input().strip())
for case in range(t):
    n = x = int(input().strip())
    if n!=0 :
        s = set()
        while len(s) < 10 :
            s.update(set(str(n)))
            n+=x
        print("Case #%d:" % (case+1),n-x)
    else : print("Case #%d:" % (case+1),"INSOMNIA")   
