# coding: utf-8

dig_all = 0b1111111111
dig = [0b1000000000,
       0b0100000000,
       0b0010000000,
       0b0001000000,
       0b0000100000,
       0b0000010000,
       0b0000001000,
       0b0000000100,
       0b0000000010,
       0b0000000001]

def Dignum(N):
    dig = 1
    while N > 9:
        N = N/10
        dig += 1
    return dig

f = open('/Users/hashimototatsuya/Downloads/A-large.in', 'r')
T = int(f.readline())
for t in range(T):
    N = int(f.readline())
    
    if int(N) == 0:
        print 'Case #%d: INSOMNIA'%(t+1)
        continue

    digofT = 0
    n = 0
    Ncopy = 0

    while 1==1:
        Ncopy = N*(n + 1)
        #print Ncopy
        dignumT = Dignum(Ncopy)
        n = n + 1
        #print n
        Ncopy2 = Ncopy
        for i in range(dignumT):
            UU = 10**(dignumT - i - 1)
            digofT = digofT|(dig[int(Ncopy2)/int(UU)])
            #print int(Ncopy2)/int(UU)
            Ncopy2 = int(Ncopy2)%int(UU)

        if digofT == dig_all:
            print 'Case #%d: %d'%(t+1,Ncopy)
            break
f.close()
