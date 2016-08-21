f = open('Counting sheep.txt', 'w')
T = int(raw_input())
for w in range(T):
    N=int(raw_input())
    a=[0,1,2,3,4,5,6,7,8,9]
    for i in range(1,10**(len(str(N))+1)):
        b=[int(j) for j in str(i*N)]
        for k in b:
            if k in a:
                a.remove(k)
        if a==[]:
            break
    print i*N
    if a==[]:
        out=i*N
    else:
        out='INSOMNIA'
    f.write("Case #"+str(w+1)+": "+str(out)+"\n")
