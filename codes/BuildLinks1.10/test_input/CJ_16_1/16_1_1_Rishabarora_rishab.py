
meramax=None
t=int(raw_input())


for k in range(1,t+1,1):
    str=raw_input()
    for i in range(0,len(str),1):
        if i==0:
            s=str[i]
            meramax=s
        else:
            if str[i]>max(s):
                s=str[i]+s
            if str[i]<max(s):
                s=s+str[i]
    print "Case #%d: %s" %(k,s)