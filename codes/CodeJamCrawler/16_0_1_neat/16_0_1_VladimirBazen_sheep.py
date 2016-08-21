def f(n):
    slo = {}
    m = n
    kok = 0
    while True:
        niz = str(m)
        for x in niz:
            if x not in slo:
                kok += 1
                slo[x] = 0
                if kok == 10:
                    break
        if kok == 10 or m > 10**7:
            break
        m += n
    return m



with open("A-large.in") as ff:
    with open("out.txt", "w") as g:
        ff.readline()
        for i,x in enumerate(ff):
            n = int(x.strip())
            print("Case #{}: {}".format(i + 1, "INSOMNIA" if n == 0 else f(n)), file = g)
