a=int(input())
j=0
while j<=a:
    j+=1
    b=input()
    k=0
    if b[0]=='-':
        k+=1
    for i in range(len(b)-1):
        if b[i]=='+' and b[i+1]=='-':
            k+=2
    print("Case #%d: %d" % (j,k))
        
            
