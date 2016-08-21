#get input
t=int(raw_input())
for i in range(1,t+1):
    temp=raw_input()
    resstr="0000000000"
    reslist=list(resstr)
    done=0
    for n in range(1,101):
        temp2=int(temp)*n
        string=str(temp2)
        for l in range(0,len(string)):
            pos=string[l]
            reslist[int(pos)]=1
            if reslist==[1,1,1,1,1,1,1,1,1,1]:
                print "Case #%d: %s" % (i,string)
                done=1
                break
        else:
            continue
        if done:
            break
    if done==0:
        print "Case #%d: INSOMNIA" % i
