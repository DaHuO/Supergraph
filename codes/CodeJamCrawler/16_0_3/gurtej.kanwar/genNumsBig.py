def tobase2(num):
    s = []
    while len(s) < 14:
        s.append(str(num%2))
        num //= 2
    return "".join(reversed(s))

divisor = "10000000000000001"
divides = []
for i in range(2,11):
    divides.append(int(divisor,i))
ds = " ".join(map(str, divides))
print "Case #1:"
for n in range(500):
    s = tobase2(n)
    s = "1"+s+"1"
    s = s+s
    print s, ds
    # Check:
    for i in range(2,11):
        assert (int(s,i) % divides[i-2] == 0), "%d %d %d" % (i, int(s,i), divides[i-2])
