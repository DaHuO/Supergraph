takein=open("input.in",'r')
giveout=open("output.txt",'w')
t=int(takein.readline())
for ca in range(1,t+1):
    n=int(takein.readline())
    hit=[False]*10
    left=10
    curr=0
    if n==0:
        curr="INSOMNIA"
    else:
        while left>0:
            curr+=n
            #do curr
            for i in range(len(str(curr))):
                ch=int(str(curr)[i])
                if hit[ch]==False:
                    hit[ch]=True
                    left-=1
    giveout.write("Case #"+str(ca)+': '+str(curr)+'\n')
takein.close()
giveout.close()
