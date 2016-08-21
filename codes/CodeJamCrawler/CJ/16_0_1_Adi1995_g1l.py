inptfile=open("A-large.in")
otptfile=open("A-large.out","w")
list1=[]
for get in inptfile:
    list1.append(get.rstrip('\n'))
a=int(list1[0])
for strt in range(1,a+1):
    nmbr=int(list1[strt])
    t1=str(strt)
    if(nmbr==0):
        otptfile.write("Case #"+t1+": "+"INSOMNIA\n")
    else:
        list2=[]
        for j in range (0,10):
            list2.insert(j,-1)
        for x in range (1,888888888):#change range
            count=0
            b=x*nmbr
            b=str(b)
            for t2 in b:
                t2=int(t2)
                list2.pop(t2)
                list2.insert(t2,t2)
            for i in range (0,10):
                if(list2[i]==i):
                    count=count+1
            if(count==10):
                bo=str(b)
                otptfile.write("Case #"+t1+": "+bo+'\n')
                break
inptfile.close()
otptfile.close()
