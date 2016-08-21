import numpy as np

def readFile(name):
    f = open("./result", 'w+')
    with open(name,"r") as mf:
        data = mf.readlines()

    
    n = int(data[0])
    k = []
    c = []
    s = []
    for da in data[1:]:
        d = da.split()
        k.append(int(d[0]))
        c.append(int(d[1]))
        s.append(int(d[2]))

    #print n,k,c,s

    for j in range(len(k)):
        st = ""
        if k[j]==1 and s[j]==1:
            st = " 1"
        elif s[j] == k[j]:
            for i in range(s[j]):
                st += " "+str(i+1)
        elif s[j]<k[j]-1 or c[j] ==1 and s[j]<k[j]:
            st = ' IMPOSSIBLE'
        else:
            for i in range(k[j]-1):
                st += " "+str(i+2)
        line = "Case #"+str(j+1)+":"+st+"\n"
        f.write(line)
