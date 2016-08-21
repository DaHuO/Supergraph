def shipcount(N):

    numlist=[i for i in range (0,10,1)]

    numset=set(numlist)

    i=1

    if (N==0) :

        return 0

    else :

        while (len(list(numset))!=0):

            x=[]

            n=i*N

            while(n!=0):

                x.append(n%10)
                n=n//10

            y=set(x)

            numset=numset-y

            i+=1

        return (i-1)*N

fp = open("A-large.in.txt", 'r')

result=[]

count = 1

for line in fp :

    if (count==1):
        T=int(line)

    else :
        dap=shipcount(int(line))

        k1="Case #{0}: ".format(count-1)

        if (dap==0):
            k2="INSOMNIA\n"

        else :
            k2="{0}\n".format(dap)

        k=k1+k2

        result.append(k)

    count+=1

    if(count==T+2):
        break

    if(count==102):
        break

f=open("result.txt", 'w')

for items in result:

    f.writelines(items)

f.close()


