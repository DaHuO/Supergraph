def numb(numbe):
    if (numbe=='0'):
        return "INSOMNIA"

    sn = {'1','2','3','4','5','6','7','8','9','0'}
    ori=int(numbe)
    while(True):
        s_num=set(numbe)
        sn = sn.difference(s_num)
        if (sn == set()):
            return numbe
        else:
            i_n = int(numbe)
            numbe = str(i_n+ori)
        
    
def sheep (file):
    f=open(file)
    g=open('output.ou',mode='w')
    b=int(f.readline()[:-1])
    for x in range(b):
        m = f.readline()[:-1]
        c=numb(m)
        g.write("Case #"+str(x+1)+": "+c+"\n")
    f.close()
    g.close()
