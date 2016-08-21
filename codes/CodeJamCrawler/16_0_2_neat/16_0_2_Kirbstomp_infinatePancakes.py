input = open("B-large.in","r+")
sol = open("sol.txt","w")
case = int(input.readline())


def solve(n):
    flipCount = 0
    cakes = []
    for x in n:
        cakes.append(x)

    while(len(cakes)>0):
        #print("U")
        while(cakes[len(cakes)-1]=='+'):
            #print("ha")
            x = cakes.pop()
            if len(cakes)==0:
                break
        if len(cakes)==0:
                break
        for p in range(0,len(cakes)):
            if cakes[p] == '-':
                cakes[p]='+'
            else:
                cakes[p]='-'
        flipCount+=1
    return flipCount
#flip(0,lol)
#print(solve("+++"))
#print(solve("---"))
for x in range(0,case):
    cakeStack = input.readline().strip()
   # print(cakeStack)
   # print(solve(cakeStack))
    sol.write("Case #"+str(x+1)+": "+str(solve(cakeStack))+'\n')