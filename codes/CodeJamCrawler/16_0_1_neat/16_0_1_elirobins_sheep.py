def sheepcount(N):
    if N==0:
        return "INSOMNIA"
    arr=['0','1','2','3','4','5','6','7','8','9']
    count=1
    while(1):
        NN=count*N
        count+=1
        for i in str(NN):
            if i in arr :
                del arr[arr.index(i)]
        if  not len(arr):
            return NN
        
a=open("A-large.in","r")
b=open("output.txt","w")
inp=list(a)
for i in range(1,int(inp[0])+1,1):
    wr="case #"+str(i)+":  "+str(sheepcount(int(inp[i])))+"\n"
    b.write(wr)
