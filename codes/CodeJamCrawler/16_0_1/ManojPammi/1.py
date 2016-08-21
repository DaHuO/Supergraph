f=open("A-large.in",'r')
p=f.readlines()
for k in range(int((p[0].split("\n"))[0])):
    i=k+1
    b=(p[i].split("\n"))[0]
    m=int(b)
    if (m==0):
        print "Case #"+str(i)+": INSOMNIA"
    else:
        y=['0','1','2','3','4','5','6','7','8','9']
        c=2
        while(y!=[]):
            u=list(b)
            y=[x for x in y if x not in u]
            b=str(m*c)
            c=c+1
        print "Case #"+str(i)+": "+str(m*(c-2))
f.close()

