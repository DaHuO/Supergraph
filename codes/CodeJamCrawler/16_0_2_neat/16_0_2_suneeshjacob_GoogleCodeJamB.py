print("started")
f=open("B-large.in.txt","r")
#f=open("B-large.in.txt","r")
g=open("output.txt", "w").close()
g=open("output.txt", "w")


T=f.readline()
N = []
    
for i in range (0,int(T)):
        N.append(f.readline())
        i2=0
        for j in range (0,len(N[i])-2):
                if N[i][j]!=N[i][j+1]:
                        i2=i2+1
        config=i2
        if (((i2%2==0)&(int(N[i][0]=='-')==1)))|(((i2%2!=0)&(int(N[i][0]=='+')==1))):
                config=config+1
        g.write("Case #")
        g.write(str(i+1))
        g.write(": ")
        g.write(str(config))
        g.write("\n")
        del config
        del i2
        

 
        
g.close()
print("completed")
