import math

def sheepCalc(n):
    if n==0:
        return 'INSOMNIA'
    inc=n
    list=[]
    while len(list)<10:
        for dig in str(n):
            if int(dig) not in list:
                list.append(int(dig))
                if len(list)==10:
                    return n
        n=n+inc

                
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    res=sheepCalc(int(raw_input()))
    print "Case #{}: {}".format(i,res)