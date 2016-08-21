t = input()

for i in range(1, t + 1):
    n = input()
    seen = map(int, str(n))
    times = 2
    count = 0
    insomnia = False
    while len(seen) < 10:
        mult = n * times
        before = len(seen)
        seen += map(int, str(mult))
        seen = list(set(seen))
        if (before == len(seen)):
            count += 1
            if count > 2000:
                insomnia = True
                break
        else:
            count = 0
        times += 1
    if insomnia:
        print "Case #" + str(i) + ": INSOMNIA"
    else:
        print "Case #" + str(i) + ": " + str(mult)

