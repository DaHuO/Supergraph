t=input()
result=[]
for z in range(0,t):

    s=raw_input()
    s=list(s)
    flg=0
    count=0
    i=0

    while i < len(s):
                #print "i1 :%d"%i
                if s[i]=='+':
                    #j=i
                    #print "i2 :%d"%i
                    while  i in range(len(s)) and s[i]!='-':
                       # j=j+1;
                       if i==len(s)-1:
                           count=flg-1
                           i=i+1
                           break
                       else:
                           s[i]='+'
                           i=i+1
                          # print "i3 :%d"%i
                    count=count+1
                    #print count
                    #i=j
                else:
                   # j=i
                    #print "i4 :%d"%i
                    while  i in range(len(s)) and s[i]!='+':
                       # j=j+1
                       s[i]='+'
                       i=i+1
                       # print "i5 :%d"%i
                    count=count+1
                    #print count
                    #i=j
                flg=count

    result.append(count)
m=1
for  y in result:
    print "Case #%d:"%m,y
    m=m+1