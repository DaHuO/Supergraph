f = open("A-large.in", "r")
j = open("o.out","w")
cases = map(int, f.read().strip().split())
for kjas in xrange(cases[0]):
    sleep = ['1','2','3','4','5','6','7','8','9','0']
    num = cases[kjas+1]
    calculate = 0
    if num == 0:
        j.write("Case #" + str(kjas+1) + ": INSOMNIA\n")
    else:
        x = 1
        while len(sleep) != 0:
            calculate = num * x
            calculate = str(calculate)
            for char in calculate:
                if char in sleep:
                    sleep.remove(char)
            x += 1
        if len(sleep) == 0:
            j.write("Case #" + str(kjas+1) + ": " + str(calculate)+"\n")
f.close()
j.close()


