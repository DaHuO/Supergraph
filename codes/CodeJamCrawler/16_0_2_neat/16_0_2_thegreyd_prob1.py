def solve(x,invert=False):
    i=len(x)-1
    ch = "+" if invert else "-"

    while(i>=0):
        if(x[i]==ch):
            break
        i-=1

    if(i==-1):
        return 0
    elif(i==0):
        return 1
    else:
        return 1+solve(x[:i],not invert)

for t in range(int(input())):
    print("Case #{}: {}".format(t+1,solve(input())))