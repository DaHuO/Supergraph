def doflip(reslist,pos):
    templist=list(reslist)
    startpos=pos
    for p in range(pos,-1,-1):
        #print reslist
        #print startpos
        #print p
        if templist[startpos-p]=="+":
            reslist[p]="-"
        else:
            reslist[p]="+"
        #print reslist

def prepareflip(reslist,pos):
    templist=list(reslist)
    startpos=pos
    for p in range(pos,-1,-1):
        #print reslist[p]
        #print startpos
        #print reslist[startpos-p]
        #print (startpos-p)
        if (reslist[p]=="-") and reslist[startpos-p]=="+":
            pass
        else:
            #print "calling on %d" % (int(startpos)-int(p)-1)
            doflip(reslist,(int(startpos)-int(p)-1))
            break
    
#read t
t=int(raw_input())
#loop on t
for i in range(1,t+1):
    #read N,K
    flips=0
    temp=raw_input()
    reslist=list(str(temp))
    for n in range(0,len(str(temp))-1):
        for m in range(n+1,len(str(temp))):
            if reslist[n]!=reslist[m]:
                flips+=1
                doflip(reslist,m-1)
                break
    if reslist[len(str(temp))-1]=="-":
        flips+=1
        doflip(reslist,len(str(temp))-1)
    print "Case #%d: %d" % (i,flips)

    
###read t
##t=int(raw_input())
###loop on t
##for i in range(1,t+1):
##    #read N,K
##    flips=0
##    temp=raw_input()
##    reslist=list(str(temp))
##    for n in range(len(str(temp))-1,-1,-1):
##        #print reslist
##        #print reslist[n]
##        if reslist[n]=="-":
##            if (reslist[0]=="+") and (n!=0):
##                #print "adding 1"
##                flips += 1
##                prepareflip(reslist,n)
##                #reslist[0]="-"
##            #print "adding 1"
##            flips += 1
##            doflip(reslist,n)
##    print "Case #%d: %d" % (i,flips)
##            
