
file_name="D-small-attempt1"
f=open(file_name+".in","r")
t=int(f.readline().strip("\n"))
f2=open(file_name+".out","w")
for i in range(1,1+t):
    k,c,s=[int(j) for j in f.readline().strip("\n").split()]
    if s<k-1 or (s==k-1 and c==1):
        f2.write("Case #"+str(i)+": "+"IMPOSSIBLE"+"\n")
    else:
        f2.write("Case #"+str(i)+":")
        if (c>1):
            if k==1:
                f2.write(" 1")

            for i2 in range(2,k+1):
                f2.write(" "+str(i2))
            f2.write("\n")
        else:
            for i2 in range(1,k+1):
                f2.write(" "+str(i2))
            f2.write("\n")

f.close()
f2.close()