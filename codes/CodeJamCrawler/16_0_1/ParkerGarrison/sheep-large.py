from math import *

def rl(l): return range(len(l))



f = open("sheep-large.out", mode='w')

T = int(input())

for nt in range(1, T+1):
    N = int(input())
    
    ans = "NONE"

            #print("p2",p2)

    if N==0:
            ans="INSOMNIA"

    if ans != "INSOMNIA":



        j = 1
        seen = [False for i in range(10)]
        while True:
            #print(N, j)

            for dig in str(j*N):
                seen[int(dig)] = True

            if all(seen):
                ans=str(j*N)
                break

            j+=1
        
    towrite = "Case #"+str(nt)+": "+str(ans)+'\n'
    f.write(towrite)
    print(towrite, end="")
    
f.close()
