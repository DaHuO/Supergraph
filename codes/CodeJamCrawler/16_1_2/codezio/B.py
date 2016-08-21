#source="C:\Users\manish\Desktop\cj\B-small-attempt0.in"
source="C:\Users\manish\Desktop\cj\B-large.in"
dest="C:\Users\manish\Desktop\cj\Output.txt"
fin=open(source)
fout=open(dest,'w')
t=fin.readline()
t=int(t)
for i in range(t):
    x = int(fin.readline())
    a=[]
    for k in range (0,2*x-1):
        b = map(int, fin.readline().split(" "))
        a=a+b
    m = []
    a=sorted(a)
    for p in a:
        if a.count(p) % 2!=0:
            m.append(p)
    m=sorted(list(set(m)))
    m=' '.join(str(z) for z in m)
    
            
    fout.write("Case #"+str(i+1)+": "+m+"\n")

fin.close()
fout.close()
