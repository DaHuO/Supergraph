def func(num, seen):
    while num!=0:
        x = num%10
        num=num/10
        if x not in seen:
            seen.add(x)
    return seen

T = input()
for x in range(0,T):
    num = input()
    seen = set()
    mul=0
    if num==0:
        print "Case #{}: {}".format(x+1,"INSOMNIA")
    else:
        while(len(seen)<10):
            mul+=1
            seen = func(num*mul,seen)
        print "Case #{}: {}".format(x+1,num*mul)
        