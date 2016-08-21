array = [0,1,2,3,4,5,6,7,8,9]
N,i,aux,u = 0, 1, 0, 0
s = False
for x in range(int(input())):
    N = int(input())
    u = N
    while(i<1000000):
        aux = N
        while(aux>0):
            array[aux%10]=-1
            aux//=10
        if max(array) == -1:
            break
        i += 1
        if aux==u*i:
            s = True
            break
        N = u*i
    if (s==True): print("Case #%d: INSOMNIA"%(x+1))
    else: print("Case #%d: %d"%(x+1,N))
    i = 0
    array = [0,1,2,3,4,5,6,7,8,9]
    s = False
