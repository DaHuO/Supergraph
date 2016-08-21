
t = int(input())
for c in range(1,t+1):
    n = int(input())
    i = n
    digits = []
    num = 0
    for j in range(1,100000):
        if len(digits) == 10:
            num = i*(j-1)
            break
        for d in str(i*j):
            if d not in digits:
                digits.append(d)
    if len(digits) != 10:
        print("Case #%d: INSOMNIA"%(c))
    else:
        print("Case #%d: %d"%(c,num))
    

