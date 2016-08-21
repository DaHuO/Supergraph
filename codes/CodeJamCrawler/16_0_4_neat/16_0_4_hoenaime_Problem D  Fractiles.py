def lecture(txt):
    pos=0
    pos2=0
    S=[]
    for k in range(2):
        car='0'
        while car!=' ':
            pos2+=1
            car=txt[pos2]
        S+=[txt[pos:pos2+1]]
        pos=pos2+1
    S+=[txt[pos2+1:]]
    return(S)
    
def main():
    ifn='D-small-attempt1.in'
    ofn='output.txt'
    f=open(ifn,'r',encoding='utf-8')
    g=open(ofn,'w')
    nb_val=int(f.readline().strip())
    for k in range(nb_val):
        enonce=f.readline().strip()
        chfr=lecture(enonce)
        g.write("Case #%d: " %(k+1))
        for j in range(chfr[0]):
            g.write("%d " %(j+1))
        g.write("\n")
    f.close()
    g.close()
    return('Fin')