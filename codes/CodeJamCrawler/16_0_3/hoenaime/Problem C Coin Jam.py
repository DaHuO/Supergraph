def chgbs(nbc,bs):
    S=0
    c=0
    nbc2=nbc[::-1]
    for k in nbc2:
        S+=int(k)*bs**c
        c+=1
    return(S)
    
def nnprem2(nb):
    trouve=False
    div=2
    premier=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,283,293,307]
    premier2=premier[::-1]
    lg=len(premier)
    while not trouve and premier2!=[]:
        div=premier2.pop()
        trouve=(nb%div==0)
    if not trouve:
        div=0
    return(div)
        
def rchch(lg,qte):
    nb=2**(lg-1)+1
    trouve=0
    S=[]
    while trouve!=qte:#Tant que pas trouve div ds tt les bases
        prem=nnprem2(nb)#Verif en base 2
        if prem!=0: #ini
            nbc2=bin(nb)[2:]
            L=[int(nbc2),prem]
            nonprem=True
            base=2
            while nonprem and base!=10:#Verif ds les autres bases
                base+=1
                prem=nnprem2(chgbs(nbc2,base))
                nonprem=(prem!=0)
                L+=[prem]
            if nonprem:
                S+=[L]
                trouve+=1
        nb+=2
    return(S)
    
def main():
    ifn='C-large.in'
    ofn='output.txt'
    f=open(ifn,'r',encoding='utf-8')
    g=open(ofn,'w')
    nb_val=int(f.readline().strip())
    for k in range(nb_val):
        enonce=f.readline().strip()
        lg=int(enonce[:3])
        qte=int(enonce[3:])
        S=rchch(lg,qte)
        g.write("Case #1:\n")
        for k in range(qte):
            for j in range(10):
                g.write("%d " %S[k][j])
            g.write("\n")
    f.close()
    g.close()
    return('Fin')