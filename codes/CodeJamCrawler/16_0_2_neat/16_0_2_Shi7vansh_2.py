with open('B-large.in') as f:
    lines = f.readlines()
def invert(s,i):
    s[0:i+1]=s[0:i+1][::-1]
    #print(s)
    while i>=0:
        if(s[i]=='+'):
            s[i]='-'
        else:
            s[i]='+'
        i=i-1
    #print(s)
    return s

for test in range(int(lines[0])):
    s=lines[test+1]
    s=list(s)
    s.pop()
    step=0
    start=0
    end=len(s)-1
    while(end>=0):
        start=0
        while(s[end]=='+' and end>=0):
            end=end-1
        if(end<0):
            break
        while(s[start]=='+'):
             start=start+1
        if(s[start]=='+' and start==0):
              step=step+1
              s=invert(s,start)
        elif(start!=0):
            if(s[start-1]=='+'):
                step=step+1
                #print(s)
                s=invert(s,start-1)
        else:
            step=step+1
            s=invert(s,end)
    print('Case #',test+1,': ',step,sep="")
