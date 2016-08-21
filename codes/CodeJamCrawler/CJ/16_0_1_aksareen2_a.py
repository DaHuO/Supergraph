t = int(input())
nums= []
while t>=1:
    tt = int(input())
    nums.append(tt)
    t=t-1
 
prod = 1
i = 1
cnt=1
for num in nums:
    lsop = [1,2,3,4,5,6,7,8,9,0]
    if num==0:
        print("Case #"+str(cnt)+":","INSOMNIA")
        cnt+=1
    else:
            i=1
            while True:
                prod=num*i
 
                temp=prod
                while prod>0:
                    d=prod%10
 
                    if d in lsop:
                        lsop.remove(d)
 
                    prod=prod//10
                if not len(lsop):
                    print("Case #"+str(cnt)+":",temp)
                    cnt+=1
                    break
                i=i+1