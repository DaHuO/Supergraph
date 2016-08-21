t = int(input())
ins = "INSOMNIA"

for x in range(t):
    n = int(input())
    n_init = n

    print("Case #" + str(x + 1) + ": ", end="")

    if n == 0:
        print(ins)
    else:
        u = [0 for y in range(10)]
        while 0 in u:
            cn = n
            while cn:
                u[cn % 10] = 1
                cn = int(cn / 10)
            n += n_init
        print(n - n_init)

