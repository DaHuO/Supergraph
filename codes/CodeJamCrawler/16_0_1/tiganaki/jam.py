f=open("input2.in","r")
T=int(f.readline())
file = open("counting_sheep.txt", "w")
if 1<=T and 100>=T:
    for k in range(int(T)):
        N=int(f.readline())
        if N==0:
            file.write("Case #")
            file.write(str(k+1))
            file.write(": INSOMNIA \n")
        if 1<=N and 1000000>=N:
            i=1
            l=[False,False,False,False,False,False,False,False,False,False]
            while l != [True,True,True,True,True,True,True,True,True,True]:
                for j in range(len(str(i*N))):
                    l[int(str(i*N)[j])]=True
                i=i+1
            file.write("Case #")
            file.write(str(k+1))
            file.write(": ")
            file.write(str((i-1)*N))
            file.write("\n")