input=open("D-small-attempt0.in","r")
output=open("PDsmall.txt","w")

T = int(input.readline())

for loop in range(T):
    K, C, S = [int(i) for i in input.readline().split()]
    
    # In the small dataset, we have S=K.
    # So we will always be able to know for sure as we just have to clean the tiles 1 to K (the original sequence).
    
    output.write("Case #{}: ".format(loop+1))
    for i in range(1,K+1):
        output.write(str(i)+" ")
    output.write("\n")

input.close()
output.close()