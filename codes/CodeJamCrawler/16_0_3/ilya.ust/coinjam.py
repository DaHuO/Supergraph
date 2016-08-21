C = 10 ** 6

def div(n):
    i = 2
    while i * i <= n and i <= C:
        if n % i == 0:
            return i
        i += 1
    return -1


def base(n, b):
    m = 0
    p = 1
    while n != 0:
        m += (n % 2) * p
        p *= b
        n //= 2
    return m


n = 32
j = 500

p = 1 << (n - 2)
q = (1 << (n - 1)) + 1

cnt = 0

lst = [0] * 15

print("Case #1:")
for mask in range(p):
    x = q + (mask << 1)

    ans = True
    for b in range(2, 11):
        d = div(base(x, b))
        lst[b] = d
        if d == -1:
            ans = False
            break

    if ans:
        cnt += 1
        for i in range(n - 1, -1, -1):
            print((x >> i) & 1, end = "")
        print(end = " ")
        for b in range(2, 11):
            print(lst[b], end = " ")
        print()
        if cnt == j:
            break

print(cnt)
