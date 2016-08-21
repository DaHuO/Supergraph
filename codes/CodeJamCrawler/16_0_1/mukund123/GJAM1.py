tc=int(raw_input())
for i in range(tc):
    n=int(raw_input())
    q=2
    if n==0:
        print "Case #"  + str(i+1)  + ": "+"INSOMNIA"
    else:
        st=str(n)
        while(1):
            if len(set(st))==10:
                final = temp
                print "Case #"  + str(i+1)  + ": "+ str(temp)
                break
            else:
               temp=q*n
               st+=str(temp)
               q+=1
