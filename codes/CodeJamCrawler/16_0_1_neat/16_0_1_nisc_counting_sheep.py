t =  int(raw_input())
for i in range(t):
    n = raw_input()
    n1 = int(n)
    if n1 == 0:
        print "Case #" + str(i+1) + ': '+ "INSOMNIA"
        continue
    d = {key: 0 for key in range(10)}
    for x in n:
        d[int(x)] = 1
    j = 2
    while sum(d.values()) < 10:
        n2 = j * n1
        for x in str(n2):
            d[int(x)] = 1
        j += 1
    print "Case #" + str(i+1) + ': '+ str(n2)
