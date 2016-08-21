input=open("A-large.in","r")
output=open("PAlarge.txt","w")

T=int(input.readline())

for loop in range(T):
    N=int(input.readline())
    l = []
    
    if N==0:
        output.write("Case #{}: INSOMNIA\n".format(loop+1))
        continue
        
    for i in range(100):
        nb = str(N*(i+1))
        for c in nb:
            if c not in l:
                l.append(c)
        if len(l)==10:
            break
    
    output.write("Case #{}: {}\n".format(loop+1,nb))
    
input.close()
output.close()