numCases=int(input())
cases=[]
for i in range(1, numCases+1):
    n=int(input())
    cases.append(n)
#print(cases)
allDigs=[0,1,2,3,4,5,6,7,8,9]
for j in range(0, len(cases)):
    digs=[]
    num=cases[j]
    origNum=cases[j]
    #print("num:", num)
    c=1
    if num==0:
        x="INSOMNIA"
    else:
        while digs!=allDigs:
            #print("digs",digs)
            #print("c",c)
            #print("num",num)
            for n in str(num):
                if int(n) not in digs:
                    digs.append(int(n))
            c+=1
            num=origNum*c
            digs.sort()
        x=origNum*(c-1)
    string="Case #"+str(j+1)+": "+str(x)
    print(string)
