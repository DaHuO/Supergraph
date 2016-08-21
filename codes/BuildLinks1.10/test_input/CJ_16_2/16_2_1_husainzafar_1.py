t=int(raw_input())
d={1:"ONE",2:"TWO",3:"THREE",4:"FOUR",5:"FIVE",6:"SIX",7:"SEVEN",8:"EIGHT",9:"NINE",0:"ZERO"}
q="6802734591"
for _i in range(t):
        print "Case #"+str(_i+1)+":",
        k=raw_input()
        s=[]
        for i in k:
                s.append(i)
        l=[]
        while(len(s)!=0):
                for j in q:
                        sub=d[int(j)]
                        f=1
                        p=s[::]
                        c=0
                        for k in sub:
                            if k in p:
                                p.remove(k)
                            else:
                                f=0
                                break
                        if(f==1):
                            l.append(j)
                            s=p[::]
                            j=q[-1]
                            break
        l.sort()
        t=""
        for i in l:
                t+=str(i)
        print t
