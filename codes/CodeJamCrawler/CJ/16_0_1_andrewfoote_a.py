num_cases = int(input())

def digits(k):
    d = 0
    while k > 0: 
        d = d | (1 << (k%10))
        k = k // 10
    return d

def solve(n):
    d = 0
    count = 0
    orig = n
    if n == 0: return "INSOMNIA"
    while True:
        d = d | digits(n)
        if d == 1023:
            return n
        n += orig

for i in range(1,num_cases+1):
    print("Case #{}:".format(i), solve(int(input())))
