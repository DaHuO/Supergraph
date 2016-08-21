def sleep(n):
    all = {}
    x = 1
    if n == 0:
        return "INSOMNIA"
    while True:
        if parse(n * x, all) >= 10:
            break
        x += 1
    return str(n * x)

def parse(n, dig):
    rem = 0
    while n > 0:
        rem = n % 10;
        n = n // 10;
        if rem not in dig:
            dig[rem] = 1
    return len(dig)

t = int(input())
for i in range(1, t+1):
    n = int(input())
    print("Case #"+ str(i) +": "+ sleep(n))