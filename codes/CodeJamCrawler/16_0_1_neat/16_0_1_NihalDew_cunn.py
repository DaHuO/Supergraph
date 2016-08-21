T=input("Enter no of test cases")
j=0
Q=['0','1','2','3','4','5','6','7','8','9']
while j<=T-1:
    j=j+1
    L=[]
    i=1
    N=input()
    while True:
        t=i*N
        t=str(t)
        L.extend(t)
        L=list(set(L))
        L.sort()
        if L==Q:
            break
        if L==['0']:
            break
            print"Insomnia"
        i=i+1
        
    if L==Q:
        print "Case #{0}:".format(j),t
    else:
        print "Case #{0}:".format(j),"Insomnia"
    
        
            
            
        
