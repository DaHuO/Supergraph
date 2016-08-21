f_in=open('2.in')
f_out=open('output.txt','w')
input=int(f_in.readline())
for kl in range(input):
    i=int(f_in.readline())
    if(i==0):
        f_out.write("case #"+str(kl+1)+": "+"INSOMNIA\n")
    else:
        list1=[]
        j=1
        while(len(list1)<10):
            m=i*j
            x=str(m)
            for k in x:
                if k not in list1:
                    list1.append(k)
            j=j+1

        f_out.write("Case #"+str(kl+1)+": "+str(m)+"\n")
f_out.close()
    
