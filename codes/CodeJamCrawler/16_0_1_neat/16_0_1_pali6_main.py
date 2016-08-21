def f(n):
    m = n
    if n == 0:
        return "INSOMNIA"
    digits = set()
    while n % 10 == 0:
        n //= 10
        digits.add('0')
    i = 1
    while len(digits) < 10: # not all(i in digits for i in range(10)):
        digits.update(set(str(n*i)))
        i += 1
    return (i-1) * m

T = int(input())

for i in range(T):
    print("Case #{}: {}".format(i + 1, f(int(input()))))
