T = int(raw_input())

def fill_digits(n, array):
    while n:
        digit = n % 10
        array[digit] = True
        n //= 10


for t in range(T):
    N = int(raw_input())
    res = N
    digits = [False for i in range(10)]
    fill_digits(N, digits)
    if N:
        while False in digits:
            res += N
            fill_digits(res, digits)
            
    else: 
        res = "INSOMNIA"
 
    print("Case #{0}: {1}".format(t+1, res))
