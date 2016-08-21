t = int(raw_input())
num = [1]*10
dub = {}
for i in range (1,t+1):
    N = raw_input()
    if int(N)==0:
        print ("Case #"+str(i)+": INSOMNIA")
        continue
    k=1
    dub = {}
    num = [1]*10
    while(len(dub)!=1):
        temp = str(int(N)*k)
        for ch in temp:
            num[int(ch)]=0
        dub = set(num)
        k +=1
    print ("Case #"+str(i)+": "+ temp)

    
    
        
