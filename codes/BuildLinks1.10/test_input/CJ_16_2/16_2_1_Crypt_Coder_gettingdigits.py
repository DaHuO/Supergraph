test=input()
ti=0
while(test):
    test-=1
    ti+=1
    s=raw_input()
    dic={0:"ZERO",1:'ONE',2:'TWO',3:'THREE',4:'FOUR',5:'FIVE',6:'SIX',7:'SEVEN',8:'EIGHT',9:'NINE'}
    ans=[]
    while(1):
        flag=0
        if 'Z' in s:
            a=dic[0]
            length=len(a)
            for i in xrange(0,length):
                s=s.replace(a[i],'',1)
            ans.append(0)
            flag=1
        if 'W' in s:
            a=dic[2]
            length=len(a)
            for i in xrange(0,length):
                s=s.replace(a[i],'',1)
            ans.append(2)
            flag=1
        if 'U' in s:
            a=dic[4]
            length=len(a)
            for i in xrange(0,length):
                s=s.replace(a[i],'',1)
            ans.append(4)
            flag=1
        if 'X' in s:
            a=dic[6]
            length=len(a)
            for i in xrange(0,length):
                s=s.replace(a[i],'',1)
            ans.append(6)
            flag=1
        if 'G' in s:
            a=dic[8]
            length=len(a)
            for i in xrange(0,length):
                s=s.replace(a[i],'',1)
            ans.append(8)
            flag=1
        if(flag==0):
            break
    while(1):
        flag=0
        if 'H' in s:
            a=dic[3]
            length=len(a)
            for i in xrange(0,length):
                s=s.replace(a[i],'',1)
            ans.append(3)
            flag=1
        if 'S' in s:
            a=dic[7]
            length=len(a)
            for i in xrange(0,length):
                s=s.replace(a[i],'',1)
            ans.append(7)
            flag=1
        if 'F' in s:
            a=dic[5]
            length=len(a)
            for i in xrange(0,length):
                s=s.replace(a[i],'',1)
            ans.append(5)
            flag=1
        if 'O' in s:
            a=dic[1]
            length=len(a)
            for i in xrange(0,length):
                s=s.replace(a[i],'',1)
            ans.append(1)
            flag=1
        if flag==0:
            break
    while(1):
        flag=0
        if 'N' in s:
            a=dic[9]
            length=len(a)
            for i in xrange(0,length):
                s=s.replace(a[i],'',1)
            ans.append(9)
            flag=1
        if flag==0:
            break
    ans.sort()
    z=''
    for ele in ans:
        z=z+str(ele)
    out='Case #'+str(ti)+': '+z
    print out
