def sleep(n):
    res = 0
    dic = {}
    for i in xrange(1,101):
        val = str(i * n)
        for x in val:
            if x not in dic:
                dic[x] = 1
        if len(dic) == 10:
            return int(val)
            break
    return "INSOMNIA"


t = int(raw_input())
for i in xrange(1, t + 1):
  n = int(raw_input())
  print "Case #{}: {}".format(i, sleep(n))
