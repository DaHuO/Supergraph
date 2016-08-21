T = eval(input())
digit = ['0','1','2','3','4','5','6','7','8','9']
for i in range(1,1+T):
    N = eval(input())
    if (N == 0):
        print("Case #{0}: INSOMNIA".format(i))
    else:
        curDigit = list(str(N))
        count = 2
        while(curDigit != digit):
            cur = N*count
            curDigit = list(set(curDigit + list(str(cur))))
            curDigit.sort()
            count+=1
        print("Case #{0}: {1}".format(i, cur))
    
