def solve(x):
    numset = {"0","1","2","3","4","5","6","7","8","9"}
    
    if(x==0):
        return "INSOMNIA"
    else:
        xset = set(str(x))
        i=2
        while(xset!=numset):
            y = x*i
            xset.update(set(str(y)))
            i+=1
        return y

for t in range(int(input())):
    print("Case #{}: {}".format(t+1,solve(int(input()))))