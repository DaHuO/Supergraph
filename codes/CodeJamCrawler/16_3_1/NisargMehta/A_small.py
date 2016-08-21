import math
def isabs(l):
    sum1 = sum(l)
    if(max(l) > math.ceil(sum1//2) and max(l) != 0):
        return True
    return False
alpha = "abcdefghijklmnopqrstuvwxyz"
tc = int(input())
for t in range(tc):
    print("Case #"+str(t+1)+": ",end="")
    n = int(input())
    l = list(map(int,input().split()))
    while(sum(l) != 0):
        maxi = max(l)
        maxind = l.index(maxi)
        l[maxind] -= 1
        output = alpha[maxind]
        #print("L : ",l)
        if(sum(l) == 0):
            print(output.upper(),end="")
            break
        maxind = l.index(max(l))
        l[maxind] -= 1
        if(isabs(l)):
            #print("here1")
            l[maxind] += 1
        else:
            #print("here2")
            output += alpha[maxind]
        #print("L1 : ",l)
        print(output.upper(),end=" ")
    print()
