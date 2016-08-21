t = int(raw_input())
for i in xrange(1, t + 1):
    k, c, s = [int(x) for x in raw_input().split(" ")]
    output = "Case #{}: ".format(i)
    for j in xrange(1, s):
        output += str(j) + " "
    output += str(s)
    print output