t=input()
count=0
result=[]
for i in range(0, t):
    num=[0,0,0,0,0,0,0,0,0,0]
    count=0
    n=input()
    if n==0:
        result.append('INSOMNIA')
    else:
        temp=n
        m=2
        while(count!=10):
            s=str(n)
           # print "s:"+s
            s=list(s)
            #print s
            s=map(int,s)
            for j in s:
                if num[j]==0:
                    num[j]=num[j]+1
                    #print num
                    count=count+1
                    if(count==10):
                        break;
                else:
                    continue;
            if(count==10):
                break
            else:
                n=temp*m
                m=m+1

        result.append(n)
    #print result

    #print s
for z in range(0,t):
    print "Case #",z,result[z]