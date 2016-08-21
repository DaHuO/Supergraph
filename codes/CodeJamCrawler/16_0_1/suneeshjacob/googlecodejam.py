print("started")
f=open("A-large.in.txt","r")
g=open("output.txt", "w").close()
g=open("output.txt", "w")


T=f.readline()
N = []
    
for i in range (0,int(T)):
        N.append(f.readline())
        N[i]=int(N[i])
        if(N[i]==0):
                g.write("Case #")
                g.write(str(i+1))
                g.write(": INSOMNIA")
                g.write("\n")
        else:
                flag=[8,8,8,8,8,8,8,8,8,8]
                flag2=str(1111111111)
                j=1
                while(''.join([str(i2) for i2 in flag])!=flag2):
                        Nt=str(j*N[i])
                        for k in range (0,len(Nt)):
                                flag[int(Nt[k])]=1
                
                        j=j+1
                Nl=(j-1)*N[i]
                g.write("Case #")
                g.write(str(i+1))
                g.write(": ")
                g.write(str(Nl))
                g.write("\n")
        
        
        
#for i in range (0,int(T)):
#        N[i]=int(N[i])



#g.write(flag)


#for i in range (0,int(T)):
#        g.write(str(N[i]))
#        g.write("\n")

        
g.close()
print("completed")
