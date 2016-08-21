testcases=raw_input()
testcases=int(testcases)
count=1
while testcases>0:
    str_in=raw_input()
    res=""
    temp=chr(ord('A')-1)
    for i in range(len(str_in)):
        if str_in[i]>=temp:
            res=str_in[i]+res
            temp=str_in[i]
        else:
            res=res+str_in[i]
    print "case #%s: %s"%(count,res)
    count=count+1
    testcases=testcases-1

