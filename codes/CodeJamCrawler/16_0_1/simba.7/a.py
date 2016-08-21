
t = eval(input())
t1 = 1
while(t > 0):
    N = eval(input())
    count = 0
    L = set()
    i = 1
    if(N <= 0):
        print("Case #",t1,": INSOMNIA",sep='')
    else:
        while(not(1 in L and 2 in L and 3 in L and 4 in L and 5 in L and 6 in L and 7 in L and 8 in L and 9 in L and 0 in L)):
            x = i * N
            I = [int(i) for i in str(x)]

            L = set(L) | set(I)
            count = x
            i += 1

    if(N != 0):
        print("Case #",t1,": ",count,sep='')
    t -= 1
    t1 += 1
