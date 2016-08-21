count = input()
for t in range(count):
    num = input()
    tut = {}
    i = 1
    if num == 0:
        print "Case #%d: INSOMNIA" % (t+1)
        continue
    while True:
        now = num * i
        for elem in list(str(now)):
            tut[elem] = 1
        if len(tut) == 10:
            print "Case #%d: %d" % (t+1, now)
            break
        i +=1
