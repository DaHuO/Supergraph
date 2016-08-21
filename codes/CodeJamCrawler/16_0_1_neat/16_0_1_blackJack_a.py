c = int(raw_input())

for idx in range(c):
    i = int(raw_input())
    if i == 0:
        print "Case #{0}: INSOMNIA".format(idx+1)
        continue
    mult = 1
    numset = set()
    while(True):
        num = i * mult
        for d in str(num):
            numset.add(d)
        if len(numset) == 10:
            print "Case #{0}: {1}".format(idx+1, num)
            break
        mult += 1
