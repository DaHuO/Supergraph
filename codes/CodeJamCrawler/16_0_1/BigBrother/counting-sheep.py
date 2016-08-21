def found(b, n):
    while n > 9:
        b |= 1 << (n % 10)
        n //= 10

    b |= 1 << (n % 10)
    return b

t = int(input())
for i in range(1, t + 1):
    n = int(input())

    if n == 0:
        print("Case #{}: INSOMNIA".format(i))
    else:
        b = 0
        c = 1

        b = found(b, n * c)
        while b != 1023:
            c += 1
            b = found(b, n * c)

        print("Case #{}: {}".format(i, n * c))
    # check out .format's specification for more formatting options
