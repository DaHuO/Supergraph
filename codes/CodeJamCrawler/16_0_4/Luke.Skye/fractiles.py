fi=open("D-small-attempt1.in","r")
fo=open("output.txt","w")
t=int(fi.readline())
t1=1
while t1<=t:
    k,c,s=map(int,fi.readline().split())
    fo.write("Case #%d: " %t1)
    for i in range(1,k+1):
        fo.write(str(i)+" ")
    fo.write("\n")

    
    t1+=1

