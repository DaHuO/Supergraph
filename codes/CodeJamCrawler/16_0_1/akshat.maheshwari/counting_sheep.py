t = input()

for i in range(t):
    n = input()
    if n == 0:
        print "Case #" + str(i + 1) + ": " + "INSOMNIA"
        continue
    s = set()
    temp = n
    s.update(list(str(temp)))
    while len(s) != 10:
        temp += n
        s.update(list(str(temp)))
    print "Case #" + str(i + 1) + ": " + str(temp)
