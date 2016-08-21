from math import *

def rl(l): return range(len(l))



f = open("a-large.out", mode='w')

T = int(input())

for nt in range(1, T+1):
    s = input()
    
    ans = s[0]

    for c in s[1:]:
        if c >= ans[0]:
            ans = c + ans
        else:
            ans += c

        
    towrite = "Case #"+str(nt)+": "+str(ans)+'\n'
    f.write(towrite)
    print(towrite, end="")
    
f.close()
