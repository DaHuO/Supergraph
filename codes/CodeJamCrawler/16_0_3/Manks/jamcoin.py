import math
def fromDigits(dd,b):
    """Compute the number given by digits in base b."""
    temp = dd
    c = 2
    n = 0
    res = 0
    while(temp != 0):
        res = (int)(res) + (((int)(temp))%c)*((int)(pow(b,n)));
        temp = (int)(((int)(temp)) / c) ;
        n = n + 1
    return res
def isprime(a):
    p = pow(a,0.5)
    i = 2
    while(i <= p):
        if(a % i == 0):
            return i
        i = i + 1
    return -1
t = (int)(input())
while (t):
    pp = (input().split(" "))
    n = (int)(pp[0])
    j = (int)(pp[1])
    c = 0
    base2 = (pow(2,n-1)) + 1 - 2;
    print ("Case #1:")
    while( c != j ):
        base2 = base2 + 2
        f2=isprime(base2)
        # print ("{0:b}".format((int)(base2)),(base3))
        if(f2 != -1):
            base3=fromDigits(base2,3)
            f3=isprime(base3)
            if(f3 != -1):
                base4=fromDigits(base2,4)
                f4=isprime(base4)
                if(f4 != -1):
                    base5=fromDigits(base2,5)
                    f5=isprime(base5)
                    if(f5 != -1):
                        base6=fromDigits(base2,6)
                        f6=isprime(base6)
                        if(f6 != -1):
                            base7=fromDigits(base2,7)
                            f7=isprime(base7)
                            if(f7 != -1):
                                base8=fromDigits(base2,8)
                                f8=isprime(base8)
                                if(f8 != -1):
                                    base9=fromDigits(base2,9)
                                    f9=isprime(base9)
                                    if(f9 != -1):
                                        base=fromDigits(base2,10)
                                        f=isprime(base)
                                        if(f != -1):
                                            c = c + 1
                                            print ("{0:b}".format((int)(base2)),f2,f3,f4,f5,f6,f7,f8,f9,f)
    t = t - 1
