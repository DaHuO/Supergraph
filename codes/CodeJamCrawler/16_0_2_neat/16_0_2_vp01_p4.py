test=input()


neg ={'+':1,
      '-':0,
      '++':1,
      '+-':1,
      '-+':2,
      '--':0}
pos ={'+':0,
      '-':1,
      '++':0,
      '+-':2,
      '-+':1,
      '--':1}

for i in xrange(test):
    s=raw_input()
    length=len(s)
    l = list(s)
    index=s[::-1].find('-')
    if index==-1:
        print "Case #%d: 0"%(i+1)
    elif length<=2:
        print "Case #%d: %d"%(i+1,pos[s])
    else:
        if l.count('-')>1:
            left=l.index('-')
            right=len(l)-l[::-1].index('-')-1
            ans=0
            state=0
            if left>0:
                ans+=1
            j=left+1
            state='-'
            while j<right:

                if l[j]!=state:
                    
                    ans+=1
                    state=l[j]
                    #print "h1 ",j,state
                j+=1
                    
            if state=='+':
                ans+=2 #for both change on left side and final -'s to +
                
            else:
                ans+=1
                
                
        else:
            if l.index('-')==0:
                ans=1

            else:
                ans=2
                
        print "Case #%d: %d"%(i+1,ans)
