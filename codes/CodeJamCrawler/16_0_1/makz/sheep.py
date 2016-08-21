for t in range(input()):
    print "Case #%s:" % str(t + 1),
    n = input()
    if n == 0 :
        print "INSOMNIA"
        continue
    seen = set(str(n))
    current = n
    while len(seen) < 10:
        current = current+n
        seen.update(str(current))
    print current