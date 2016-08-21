# Counting Sheep Small input

t = int(input())  
for k in range(1, t + 1):
    n = input()
    if n=='0':
        print("Case #"+str(k)+": INSOMNIA")
    else:
        awake = True
        required = ['0','1','2','3','4','5','6','7','8','9']
        times=2
        num=n
        while awake:
            for i in range(len(num)):
                for j in range(len(required)):
                    if required[j]==num[i]:
                        required.remove(num[i])
                        break
            if required==[]:
                awake=False
                print("Case #"+str(k)+": "+num)
            else:
                num=int(n)*times
                num=str(num)
                times+=1
