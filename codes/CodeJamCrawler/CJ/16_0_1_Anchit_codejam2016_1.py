
inf=open("C:\\Users\\Anchit\\Downloads\\code jam\\test.txt")

t=int(inf.readline())
output=[]
for i in range(t):
    count=1
    n=int(inf.readline())    
    ml=[]
    def sleep1():
        global count
        res=0
        n1=count*n
        count+=1
        n_str=str(n1)
        global ml
        for i in n_str:
            if i not in ml:
                ml.append(int(i))
        for j in range(10):
            if j in ml:
                res+=1

        if res==10:
            output.append(n_str)
        else:
            sleep1()
        
    if n==0:
        output.append('INSOMNIA')
    else:
        sleep1()
inf.close()
outf=open('C:\\Users\\Anchit\\Downloads\\code jam\\test_output.txt','w')
for i in range(t):
    outf.write('Case #'+str(i+1)+': '+str(output[i])+'\n')
outf.close()
        
