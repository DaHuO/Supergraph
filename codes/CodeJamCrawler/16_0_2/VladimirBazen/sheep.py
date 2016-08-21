def f(sez):
    s = [1 for i in range(len(sez))]
    i = len(sez) - 1
    m = 0
    while i >= 0:
##        print(s,i)
        if s[i] == sez[i]:
##            print("ok")
            i -=1
        else:
##            print("popravek")
            for j in range(i + 1):
                s[j] = 1 - s[j]
            i -= 1
            m += 1
    return m



with open("B-large.in") as ff:
    with open("out.txt", "w") as g:
        ff.readline()
        for i,x in enumerate(ff):
##            print(x.strip())
            sez = [int(y == "+") for y in x.strip()]
            print("Case #{}: {}".format(i + 1, f(sez)), file = g)
