def count(n):
    digs = set("1234567890")
    if n == 0:
        return "INSOMNIA"
    i = 1
    while digs:
        digs.difference_update(str(n*i))
        i += 1
    return n*(i-1)

t = int(raw_input().strip())
for i in range(t):
    print "Case #{}: {}".format(i+1,count(int(raw_input().strip())))
