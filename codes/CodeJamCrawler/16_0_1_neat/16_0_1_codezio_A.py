#source="C:\Users\Mani\Desktop\A-small-attempt0.in"
source="C:\Users\manish\Desktop\cj\A-large.in"
dest="C:\Users\manish\Desktop\cj\Output.txt"
fin=open(source)
fout=open(dest,'w')
t=fin.readline()
t=int(t)
for i in range(t):
    x = int(fin.readline())
    a = []
    k = 1
    p=x
    while len(a)!=10:
        if p==0:
            ans = 'INSOMNIA'
            break
        p = k*x
        k = k+1
        p = str(p)
        for b in p:
            if b not in a:
                a.append(b)
        ans = p


    fout.write("Case #"+str(i+1)+": "+ans+"\n")
fin.close()
fout.close()
