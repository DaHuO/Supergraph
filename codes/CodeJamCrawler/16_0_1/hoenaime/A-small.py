def rchch(nbc):
    L=[]
    mult=int(nbc)
    if mult==0:
        return('INSOMNIA')
    while len(L)!=10:
        for c in nbc:
            if not (c in L):
                L.append(c)
        nbc=str(mult+int(nbc))
    return(int(nbc)-mult)

def main():
    ifn='A-large.in'
    ofn='output.txt'
    f=open(ifn,'r',encoding='utf-8')
    g=open(ofn,'w')
    nb_val=int(f.readline().strip())
    for k in range(nb_val):
        nbc=f.readline().strip()
        S=rchch(nbc)
        if S=='INSOMNIA':
            g.write("Case #%d: " %(k+1))
            g.write("INSOMNIA\n" )
        else:
            g.write("Case #%d: " %(k+1))
            g.write("%d\n" %S)
    f.close()
    g.close()
    return('Fin')
    
