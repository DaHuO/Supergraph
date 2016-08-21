def rchch(lst):
    nb2=0
    for k in lst:
        nb2+=k
    S=[]
    while nb2!=2:
        nb2-=2
        (m,i)=maxi(lst)
        lst[i]=lst[i]-1
        (n,j)=maxi(lst)
        lst[j]=lst[j]-1
        (o,k)=maxi(lst)
        if o>nb2/2:
            S+=[(i,-1)]
            lst[j]=lst[j]+1
            nb2+=1
        else:
            S+=[(i,j)]
    (m,i)=maxi(lst)
    lst[i]=lst[i]-1
    (n,j)=maxi(lst)
    lst[j]=lst[j]-1
    S+=[(i,j)]
    return(S)

def maxi(L):
    a=L[0]
    l=len(L)
    i=0
    for k in range(1,l):
        if a<L[k]:
            a=L[k]
            i=k
    return(a,i)


def lecture(txt,nb):
    c=0
    c1=0
    arret=0
    S=[]
    while arret!=nb-1:
        c+=1
        if txt[c]==' ':
            arret+=1
            S+=[txt[c1:c]]
            c1=c+1
    S+=[txt[c1:]]
    return(S)
    
def main():
    ifn='A-large.in'
    ofn='output.txt'
    f=open(ifn,'r',encoding='utf-8')
    g=open(ofn,'w')
    nb_val=int(f.readline().strip())
    for k in range(nb_val):
        g.write("Case #%d:" %(k+1))
        nbc=int(f.readline().strip())
        txt=lecture(f.readline().strip(),nbc)
        S=rchch(list(map(lambda x:int(x),txt)))
        for j in S:
            g.write(" ")
            for i in j:
                if i!=-1:
                    g.write("%s" %chr(i+97).upper())
        g.write("\n")
    f.close()
    g.close()
    return('Fin')
    