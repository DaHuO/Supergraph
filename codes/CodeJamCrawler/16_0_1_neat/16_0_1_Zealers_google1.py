f1=open("A-large.in")
f2=open("A-large.out","w")
san=[]
for get in f1:
    san.append(get.rstrip('\n'))
a=int(san[0])
for start in range(1,a+1):
    num=int(san[start])
    t1=str(start)
    if(num==0):
        f2.write("Case #"+t1+": "+"INSOMNIA\n")
    else:
        sun1=[]
        for i in range (0,10):
            sun1.insert(i,12)
        for j in range (1,1000001):
            t4=0
            t3=j*num
            t3=str(t3)
            for t2 in t3:
                t2=int(t2)
                sun1.pop(t2)
                sun1.insert(t2,t2)
            for k in range (0,10):
                if(sun1[k]==k):
                    t4=t4+1
            if(t4==10):
                t5=str(t3)
                f2.write("Case #"+t1+": "+t5+'\n')
                break
f1.close()
f2.close()
