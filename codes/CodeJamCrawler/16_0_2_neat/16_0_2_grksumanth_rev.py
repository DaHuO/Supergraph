fp=open('B-large.in','r')
fla='0'
val=1
flap=0
def reve(y,x):
    z=[]
    
    #print "entered reve",y
#    print 'x :',x
    for k in range(x):
 #       print 'x-k',x-k
  #      print 'y',y
   #     print 'x-k-1: ',x-k-1
        if y[x-k-1]=='-':
            z.append('+')
        else:
            z.append('-')
     #   print 'z',z
#    print 'x+1',x+1
 
    for tr in y[x:]:
        z.append(tr)
 #   print 'leaving reve',z
    return z
def che(y,count):
    flag9=0
    global val
    for z in y:
        if z=='-':
            flag9=1
            return 0
    if flag9==0:
        print 'Case #%d: %d'%(val,count)
        val+=1
        return 1
def cou(x):
    global val
    flap=0
    y=[]
    count=0
    for z in x:
        y.append(z)
    leny= len(y)
#    print 'entered y is :  ',''.join(y)
    if che(y,0):
        return
    if leny==1:
        if y[0]=='-':
            print 'Case #%d: 1'%(val)
            val+=1
        elif y[0]=='+':
            #print 'this case'
            print 'Case #%d: 0'%(val)
            val+=1
        return
    if leny==2:
        if y[0]=='+' and y[0]==y[1]:
            print 'Case #%d: 0'%(val)
        elif y[0]=='-' and y[0]==y[1]:
           # print"has"
            print 'Case #%d: 1'%(val)
        elif y[0]=='-' and y[0]!=y[1]:
            print 'Case #%d: 1'%(val)
        else:
            print 'Case #%d: 2'%(val)
        val+=1
        return
    for x in range(leny):
     #   print 'y[0] is : ',y[0],'y',[leny-x-1],':',y[leny-x-1],'y',[leny-1],':',y[leny-1]
        if y[leny-x-1]==y[0] and y[leny-x-1]=='-':
#            print 'entered - -'
 #           print "before rev",y
            y=reve(y,leny-x+flap)
            count+=1
            flap=0
            if che(y,count):
                return
        elif y[leny-x-1]==y[0] and y[leny-x-1]=='+':
   #         print 'entered + +'
           pass
            
        elif y[leny-x-1]!=y[0] and y[leny-x-1]=='-':
  #          print 'entered + -'
   #         print leny-x-1
            if y[0]=='+' and y[0]!=y[1]:
                count+=2
                y[1]='+'
                if che(y,count):
                    return
                else:
                    y[1]='-'
                    count-=2
            for temp in range(leny-x):
    #            print 'temp',temp
                if y[temp]=='-':
                    y=reve(y,temp)
                    count+=1
                    flap=1
                    break
            y=reve(y,leny-x)
            count+=1
            if che(y,count):
                return
        elif y[leny-x-1]!=y[0] and y[leny-x-1]=='+':
     #       print 'entered - +'
            for temp in range(leny-x-1):
                if y[temp]=='+':
                    y=reve(y,temp)
                    count+=1
                    break
            if y[0]=='-' and y[0]!=y[1]:
                count+=1
                y[0]='+'
            if che(y,count):
                return
for x in fp:
    if fla=='0':
        fla='1'
        pass
    else:
        cou(x.strip())
