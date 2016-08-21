input=open("A-small-attempt0.in","r")
output=open("PAsmall.txt","w")

T = int(input.readline())

for loop in range(T):
    N = int(input.readline())
    P = [int(x) for x in list(input.readline().split())]
    
    output.write("Case #{}: ".format(loop+1))
    c = 0
    while P!=[1]*N:        
        M = P.index(max(P))
        P[M]-=1
        output.write(chr(ord('A')+M))
        
        if c%2==1:
            output.write(" ")
        c+=1
    
    if c%2==0:
        output.write(" "
    
    if N%2==0:
        for j in range(0,N-1,2):
            output.write(chr(ord('A')+j))
            output.write(chr(ord('A')+j+1))
        output.write(" ")
    else:
        output.write("A ")
        for j in range(1,N-1,2):
            output.write(chr(ord('A')+j))
            output.write(chr(ord('A')+j+1))
        output.write(" ")
    
    output.write("\n")

input.close()
output.close()
