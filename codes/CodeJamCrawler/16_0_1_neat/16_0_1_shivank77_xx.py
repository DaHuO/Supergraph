t = int(input())  
for i in range(1, t + 1):
    m = int(input())
    myset = {0,1,2,3,4,5,6,7,8,9}
    count = 1
    if m==0:
        print("Case #{}: {}".format(i,'INSOMNIA'))
    else :
        new = [int(x) for x in str(m)]
        c = set(new)
        while c!=myset:
            count +=1
            n = count*m
            c = set().union(*[c,[int(x) for x in str(count*m)]])
        print("Case #{}: {}".format(i, n))
    
