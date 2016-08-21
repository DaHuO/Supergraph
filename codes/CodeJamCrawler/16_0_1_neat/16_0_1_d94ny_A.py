
def insomia(n):
    return n == 0

t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    print "Case #{0}:".format(i+1),

    # TODO : this is stupid
    if insomia(n):
        print "INSOMNIA"
        continue

    # Cycle through it?
    f = n
    seen = [False]*10
    while False in seen:
        for x in str(f):
            seen[int(x)] = True

        f += n
    print f - n
