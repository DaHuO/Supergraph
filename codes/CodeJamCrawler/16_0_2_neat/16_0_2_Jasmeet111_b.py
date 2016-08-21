# cook your code here
t=input()
for k in xrange(t):
    n=raw_input()
    length=len(n)
    count=0


    or i in xrange(1,length-1):
        if n[i]!=n[i-1]:
            count=count+1

    if n[length-1]=='-' and n[length-2]=='+':
        count=count+2
    elif n[length-1]=='-':
        count=count+1
    elif n[length-1]=='+' and n[length-2]=='-':
        count=count+1
    print "Case #"+str(k+1)+": "+str(count)