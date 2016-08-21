def fill(num,arr):
    while(num>0):
        s=num%10
        num=num//10
        arr[s]=1

def filled(arr):
    for i in arr:
        if(i==0):
            return False
    return True

num=int(input())
for i in range(1,num+1):
    n=int(input())
    if(n==0):
        print("Case #"+str(i)+": "+"INSOMNIA")
        continue
    arr=[0]*10
    num=n
    while(True):
        fill(num,arr)
        if(filled(arr)):
            break
        num+=n
    print("Case #"+str(i)+": "+str(num))


