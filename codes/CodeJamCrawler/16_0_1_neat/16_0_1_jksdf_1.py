def casePrint(n, v):
    print("Case #{}: {}".format(n, v))

def f(number):
    v = int(input())
    if v == 0:
        casePrint(number, "INSOMNIA")
        return;
    k = 0
    digits = [0 for i in range(10)]
    while digits.count(0) != 0:
        k += v
        for j in str(k):
            digits[int(j)]+=1
    casePrint(number, k)
    return;
        
    

N = int(input())
for n in range(N):
    f(n+1)
