tst=int(raw_input())
for tst in range(0,tst):
    i=raw_input()
    t=list(i)
    d={0:"ZERO",1:"ONE",2:"TWO",3:"THREE",4:"FOUR",5:"FIVE",6:"SIX",7:"SEVEN",8:"EIGHT",9:"NINE"}
    z=""
    cx=[0,2,4,6,8,5,9,7,3,1]
    count=0
    while len(t)>0:
        for u in range(0,10):
          flag=1
          while flag!=0:  
            i=cx[u]
            p=list(d[i])
            m=list(t)
            #print m
            #print z
            for c in p:
            
                if c in m:
                    x=m.index(c)
                    del m[x]
                    flag=1
                
                else:
                    flag=0
                    break

            if flag==1:
                z=z+str(i)
                for k in p:
                    if k in t:
                        x=t.index(k)
                        del t[x]

          count=count+1
          #print count
          #print t
          if count==9 and len(t)!=0:
                count=0
                i=-1
            
    res=list(z)
    res.sort()
    print "Case #%d: %s"%(tst+1,''.join(res))
    
