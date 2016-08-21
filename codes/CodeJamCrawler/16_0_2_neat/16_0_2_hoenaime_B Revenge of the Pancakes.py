def rchch(nbc):
    S=0
    prec=nbc[0]
    for c in nbc:
        if c!=prec:
            S+=1
            prec=c
    if nbc[-1]=='-':
        S+=1
    return(S)

def main():
    ifn='B-large.in'
    ofn='output.txt'
    f=open(ifn,'r',encoding='utf-8')
    g=open(ofn,'w')
    nb_val=int(f.readline().strip())
    for k in range(nb_val):
        nbc=f.readline().strip()
        S=rchch(nbc)
        g.write("Case #%d: " %(k+1))
        g.write("%d\n" %S)
    f.close()
    g.close()
    return('Fin')