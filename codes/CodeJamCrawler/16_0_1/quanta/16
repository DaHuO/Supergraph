t=int(raw_input())
for i in range(1,t+1):
    lista=[0,1,2,3,4,5,6,7,8,9]
    m=0
    l=0
    n = int(raw_input())
    g=0
    while m !=10:
        if n == 0:
            print"Case #%d: INSOMNIA" %(i)
            break
        if g==0:
            l+=1
            g =n*l
        for a in range(len(lista)):
            if lista[a] == g%10:
                lista[a]=-1
                m+=1
                break
        g/=10
        print g,m
    print "Case #%d: %s" %(i, n*l)
        
