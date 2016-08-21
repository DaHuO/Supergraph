def main():
    t= int(input())
    for i in range(t):
        rank=[False for x in range(0,10)]
        insomnia=False
        cont=0
        acabo = False
        nprev = 0
        n = input()
        ntemp = int(n)
        s = 2
        while not insomnia and not acabo:
            cont+=1
            for j in n:
                rank[int(j)]=True
            acabo=True
            for k in rank:
                if(k==False):
                    acabo=False
                    break
            if((n!="0" and cont>1 and nprev/int(n)==0) or nprev==int(n)):
                insomnia=True
            nprev=int(n)
            n=str(ntemp*s)
            s+=1
        if insomnia:
            print("Case #"+str(i+1)+": INSOMNIA")
        else:
            print("Case #"+str(i+1)+":",nprev)

main()
