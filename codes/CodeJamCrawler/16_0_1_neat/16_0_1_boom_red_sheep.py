f=open('A-large.in', 'r')
N=[]
i=0
for line in f:
    if i==0:
        T=int(line)
    else:
        N.append(int(line))
    i=i+1
R=0
for j in range(len(N)):
    ans={0,1,2,3,4,5,6,7,8,9}
    counting_digit=[]
    k=1
    trigger=True
    R=R+1
    while trigger:
        if N[j]==0:
            Y='INSOMNIA'
            if R==1:
                fo=open('output.txt', 'w')
                fo.write('Case #'+str(R)+': '+str(Y)+'\n')
            else:
                fo=open('output.txt', 'a')
                fo.write('Case #'+str(R)+': '+str(Y)+'\n')
            fo.close()
            break
        else:
            product=str(k*N[j])
            #print counting_digit
            Y=product
            for l in product:
                for m in ans:
                    if int(l)==m and (int(l) in counting_digit)==False:
                        counting_digit.append(int(l))
            if len(counting_digit)==10:
                trigger=False
                if R==1:
                    fo=open('output.txt', 'w')
                    fo.write('Case #'+str(R)+': '+str(Y)+'\n')
                else:
                    fo=open('output.txt', 'a')
                    fo.write('Case #'+str(R)+': '+str(Y)+'\n')
                fo.close()
                break
        k=k+1
        
    
