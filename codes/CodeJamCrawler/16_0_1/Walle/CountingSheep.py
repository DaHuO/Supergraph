def digits(n):
    while n:
        digit = n % 10
        n //= 10
        yield digit


t = int(raw_input())

for i in xrange(1, t + 1):
    found = False
    n = int(raw_input())
    
    if n == 0:
        print "Case #{}: {}".format(i, "INSOMNIA")
        continue

    if n == 1:
        print "Case #{}: {}".format(i, "10")
        continue

    seen = [0]*10
    for j in xrange(1, 73):
        x = n*j
        for digit in digits(x):
            seen[digit] = 1

        if sum(seen) == 10:
            print "Case #{}: {}".format(i, x)
            found = True
            break

    if found == True:
        continue

    print "Case #{}: {}".format(i, "INSOMNIA")

