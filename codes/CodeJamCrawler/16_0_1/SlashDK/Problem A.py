def getints(n):
    digits=set()
    while(n!=0):
        digits.add((n%10))
        n=n//10
    return digits


t=input()
for i in range (0,int(t)):
    n=input()
    n=int(n)
    k=0
    if(n==0):
        print("Case #"+str(i+1)+": INSOMNIA")
        continue
    nums=set(list(range(0, 10)))
    while(len(nums)!=0):
        k+=1
        nums-=getints(n*k)
        #print(nums,n*k)
    print("Case #"+str(i+1)+": " + str(n*k))
        
