input=open("C-small-attempt1.in","r")
output=open("PCsmall.txt","w")

T = int(input.readline())

def div(n):
    if n == 1:
        return 1
    
    if n == 2:
        return -1

    for loop in range(3,int(n**0.5)+1,2):
        if n%loop == 0:
            return loop
    return -1

for loop in range(T):
    N, J = [int(i) for i in input.readline().split()]
    
    nb = bin(2**(N-1)+1)[2:]
    add = 2
    n = 0
    output.write("Case #{}: \n".format(loop+1))
    
    while n != J:
        print(n)
        l = []
        
        for i in range(2,11):
            l.append(div(int(nb,i)))
        
        c = 0
        if -1 not in l:
            output.write(nb+" ")
            for d in l:
                output.write(str(d)+" ")
            output.write("\n")
            
            n += 1
        
        nb = bin(int(nb,2)+add)[2:]

input.close()
output.close()