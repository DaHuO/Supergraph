import sys


# For small input...

def coin():
    # We divide into cases.
    # (d^15 + 1) + d(d + 1)
    # (d^15 + 1) + d*d*(d+1)
    # ...
    # (d^15 + 1) + d^13(d + 1)

    num = {}
    
    l1 = []

    M = pow(10, 15) + 1

    a = 10*11
    i = 1
    while i <= 13:
        x = M + a
        l1.append(x)
        a = 10*a
        i += 1

    divisors = []
    for d in xrange(2, 11):
        divisors.append(d + 1)

    ans = {}
    for i in l1:
        ans[i] = divisors


    for i in xrange(len(l1)):
        m = []
        m.append(l1[i])
        m = m + divisors
        num[i] = m

    #return num

    

        


    #ans1 = [11]*len(l1)

    # (d^15 + 1) + d*(d^3 + 1)
    # (d^15 + 1) + d*d*(d^3 + 1)
    #  ...

    l2 = []

    i = 1
    a = 1001*10
    while i <= 10:
        x = M + a
        l2.append(x)
        a = a*10
        i += 1

    divisors = []
    for d in xrange(2, 11):
        divisors.append(d*d*d + 1)

    #ans = {}
    for i in l2:
        ans[i] = divisors

    for i in xrange(len(l2)):
        m = []
        m.append(l2[i])
        m = m + divisors
        num[i + len(l1)] = m

    #return num



    # (d^15 + 1) + d*(d^5 + 1)
    #....

    l3 = []
    i = 1
    a = 100001*10
    while i <= 9:
        x = M + a
        l3.append(x)
        a = a*10
        i += 1

    divisors = []
    for d in xrange(2, 11):
        divisors.append(d*d*d*d*d + 1)

    #ans = {}
    for i in l3:
        ans[i] = divisors

    for i in xrange(len(l3)):
        m = []
        m.append(l3[i])
        m = m + divisors
        num[i + len(l1) + len(l2)] = m

   

    # (d^15 + d^13) + (d^2 + 1)
    

    N = pow(10, 15) + pow(10,13)
    

    l4 = []
    i = 1
    
    a = 101
    x = N + a
    l4.append(x)

    divisors = []
    for d in xrange(2, 11):
        divisors.append(d*d + 1)

    #ans = {}
    for i in l4:
        ans[i] = divisors


    for i in xrange(len(l4)):
        m = []
        m.append(l4[i])
        m = m + divisors
        num[i + len(l1) + len(l2) + len(l3)] = m

    # (d^15 + d^11) + (d^4 + 1)

    N = pow(10, 15) + pow(10,11)

    l5 = []
    i = 1
    
    a = 10001
    x = N + a
    l5.append(x)

    #ans5 = [10001]*len(l5)
    divisors = []
    for d in xrange(2, 11):
        divisors.append(d*d*d*d + 1)

    #ans = {}
    for i in l5:
        ans[i] = divisors
        
    for i in xrange(len(l5)):
        m = []
        m.append(l5[i])
        m = m + divisors
        num[i + len(l1) + len(l2) + len(l3) + len(l4)] = m




    l = l1 + l2 + l3 + l4 + l5


    #/..........
    l6 = []
    i = 1
    M = pow(10, 15) + pow(10, 8) + pow(10, 7) + 1
    
    a = 100*10000001
    while i <= 5:
        x = M + a
        l6.append(x)
        a = a*10
        i += 1

    divisors = []
    for d in xrange(2, 11):
        divisors.append(d + 1)

    #ans = {}
    for i in l6:
        ans[i] = divisors

    for i in xrange(len(l6)):
        m = []
        m.append(l6[i])
        m = m + divisors
        num[i + len(l1) + len(l2) + len(l3) + len(l4) + len(l5)] = m

    l = l + l6

    #/////////////

    l7 = []
    i = 1
    #M = pow(10, 15) + pow(10, 8) + pow(10, 7) + 1
    
    a = 10*100000001
    while i <= 6:
        x = M + a
        l7.append(x)
        a = a*10
        i += 1

    divisors = []
    for d in xrange(2, 11):
        divisors.append(pow(d,8) + 1)

    #ans = {}
    for i in l7:
        ans[i] = divisors

    for i in xrange(len(l7)):
        m = []
        m.append(l7[i])
        m = m + divisors
        num[i + len(l1) + len(l2) + len(l3) + len(l4) + len(l5) + len(l6)] = m

    l = l + l7

    #-----------

    l8 = []
    i = 1
    M = pow(10, 15) + pow(10, 10) + pow(10, 5) + 1
    
    a = 100001*10
    while i <= 4:
        x = M + a
        l8.append(x)
        a = a*10
        i += 1

    divisors = []
    for d in xrange(2, 11):
        divisors.append(d + 1)

    #ans = {}
    for i in l8:
        ans[i] = divisors

    for i in xrange(len(l8)):
        m = []
        m.append(l8[i])
        m = m + divisors
        num[i + len(l1) + len(l2) + len(l3) + len(l4) + len(l5) + len(l6) + len(l7)] = m

    #Lastly,.... d^15 + 1

    l9 = []
    i = 1
    M = pow(10, 15) + 1
    
    #a = 100001
    #x = M + a
    l9.append(M)
        
    divisors = []
    for d in xrange(2, 11):
        divisors.append(d + 1)

    #ans = {}
    for i in l8:
        ans[i] = divisors

    for i in xrange(len(l9)):
        m = []
        m.append(l9[i])
        m = m + divisors
        num[i + len(l1) + len(l2) + len(l3) + len(l4) + len(l5) + len(l6) + len(l7) + len(l8)] = m

    l = l + l8 + l9




    return num

    




    #return num

    
    


ans = coin()
T = int(sys.stdin.readline())
for i in xrange(T):
    N, J = map(int, sys.stdin.readline().split(' '))
    s = 'Case #1:'
    print s
    for j in xrange(len(ans)):
        s = ''
        for l in ans[j]:
            s += str(l) + ' '
        print s
            
