checklst=[0,1,2,3,4,5,6,7,8,9]
f=open('sheep2.in','r')
newf=open('result.txt','w')
s=f.read()
T=int(s.split()[0])
for i in range (1,T+1):
    N=s.split()[i]
    cntlst=[]
    it=1
    counter=1
    presentnumber=N
    while counter>0:
        if presentnumber=='0':
            newf.write('Case #'+str(i)+': '+'INSOMNIA')
            newf.write("\n")
            break
        for k in presentnumber:
            if int(k) in checklst:
                cntlst.append(int(k))
        it+=1
        counter+=1
        if list(set(cntlst))==checklst:
            print 'Case #'+str(i)+': '+presentnumber
            newf.write('Case #'+str(i)+': '+presentnumber)
            newf.write("\n")
            '''
            newf.write('Case #')
            newf.write(str(i))
            newf.write(': ')
            newf.write(presentnumber)
            '''
            break
        presentnumber=str(int(N)*it)
newf.close()

