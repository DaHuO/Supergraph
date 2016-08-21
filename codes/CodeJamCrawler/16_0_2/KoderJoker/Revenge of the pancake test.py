f=open('pancake2.in','r')
newf=open('result.txt','w')
s=f.read()
T=int(s.split()[0])
for i in range (1,T+1):
    stack=list(s.split()[i])
    cnt=0
    for k in range (len(stack)-1): #checking if next pancake is same or not, else flipping
        if stack[k]==stack[k+1]: #when nearby pancake is same
            pass
        elif stack[k]!=stack[k+1]: #when nearby pancake is not same
            flipping=stack[:k+1]
            flipping=flipping[::-1]
            for l in range (len(flipping)):
                if flipping[l]=='-':
                    flipping[l]='+'
                elif flipping[l]=='+':
                    flipping[l]='-'
            stack=flipping+stack[k+1:]
            cnt+=1
    if stack[0]=='-':
        cnt+=1
    print 'Case #'+str(i)+': '+str(cnt)
    newf.write('Case #'+str(i)+': '+str(cnt))
    newf.write("\n")
newf.close()

