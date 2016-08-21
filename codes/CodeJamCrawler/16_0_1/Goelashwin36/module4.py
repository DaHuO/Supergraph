readf=open('A-large.in','r') # replace input.in with your file name

x=readf.read()

t=int(x.split()[0])
f=open('abc.txt','w')
k=0
for i in range(1,t+1):

    n=int(x.split()[i])

    a=n
    z=0
    l=[]
    j=2

    while l.count('0')==0 or l.count('1')==0 or l.count('2')==0 or l.count('3')==0 or l.count('4')==0 or l.count('5')==0 or l.count('6')==0 or l.count('7')==0 or l.count('8')==0 or l.count('9')==0:
        for i in str(a):
            l.append(i)
        a=n*j
        if a==n*(j-1):
            z='INSOMNIA'
            break
        j=j+1



    else:z=str( n*(j-2))
    k=k+1
    f.write('Case #'+str(k)+': '+z+'\n')
