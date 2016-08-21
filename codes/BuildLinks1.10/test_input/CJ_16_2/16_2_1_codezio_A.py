#source="C:\Users\manish\Desktop\cj\A-small-attempt0.in"
source="C:\Users\manish\Desktop\cj\A-large.in"
dest="C:\Users\manish\Desktop\cj\Output.txt"
fin=open(source)
fout=open(dest,'w')
t=fin.readline()
A = ['ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
t=int(t)
for i in range(t):
    a = [0]*10
    x = (fin.readline())
    p=x.count('W')
    if p>0:
        a[2]=p
        x=x.replace('T','',p)
        x=x.replace('W','',p)
        x=x.replace('O','',p)
    p=x.count('G')
    if p>0:
        a[8]=p
        x=x.replace('E','',p)
        x=x.replace('I','',p)
        x=x.replace('G','',p)
        x=x.replace('H','',p)
        x=x.replace('T','',p)
    p=x.count('X')
    if p>0:
        a[6]=p
        x=x.replace('S','',p)
        x=x.replace('I','',p)
        x=x.replace('X','',p)
    p=x.count('U')
    if p>0:
        a[4]=p
        x=x.replace('F','',p)
        x=x.replace('O','',p)
        x=x.replace('U','',p)
        x=x.replace('R','',p)
    p=x.count('Z')
    if p>0:
        a[0]=p
        x=x.replace('Z','',p)
        x=x.replace('E','',p)
        x=x.replace('R','',p)
        x=x.replace('O','',p)
    p=x.count('H')
    if p>0:
        a[3]=p
        x=x.replace('T','',p)
        x=x.replace('H','',p)
        x=x.replace('R','',p)
        x=x.replace('E','',2*p)
    p=x.count('O')
    if p>0:
        a[1]=p
        x=x.replace('O','',p)
        x=x.replace('N','',p)
        x=x.replace('E','',p)
    p=x.count('F')
    if p>0:
        a[5]=p
        x=x.replace('F','',p)
        x=x.replace('I','',p)
        x=x.replace('V','',p)
        x=x.replace('E','',p)
    p=x.count('S')
    if p>0:
        a[7]=p
        x=x.replace('S','',p)
        x=x.replace('E','',p)
        x=x.replace('V','',p)
        x=x.replace('E','',p)
        x=x.replace('N','',p)
    p=x.count('E')
    if p>0:
        a[9]=p
        x=x.replace('N','',p)
        x=x.replace('I','',p)
        x=x.replace('N','',p)
        x=x.replace('E','',p)

    w=""
    for d in range(0,10):
        w = w+str(d)*a[d]
    fout.write("Case #"+str(i+1)+": "+w+"\n")

fin.close()
fout.close()
