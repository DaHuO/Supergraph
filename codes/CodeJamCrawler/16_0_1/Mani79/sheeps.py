from sys import stdin

T = int(stdin.readline())

for k in range(T):
    N = int(stdin.readline())
    if N==0:
        print('Case #' + str(k+1) + ": INSOMNIA")
        continue
    digits = [False]*10
    
    i = 1
    iN = N
    while True:
        for d in str(iN):
            digits[int(d)]=True
        if all(digits):
            break
        else: 
            iN = iN+N
            i = i+1

    print('Case #' + str(k+1) + ": " + str(iN))        

