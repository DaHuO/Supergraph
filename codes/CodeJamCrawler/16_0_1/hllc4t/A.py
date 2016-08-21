
inputfile, outfile = None, None

t = int(raw_input())

for tnum in xrange(1, t+1):
    dig_set = set()
    n = int(raw_input())
    
    if n is 0:
        print "Case #{}: INSOMNIA".format(tnum)
        continue

    i = 1
    while True:
        dig_set.update(list(str(n * i)))
        if len(dig_set) == 10:
            break
        i += 1

    print "Case #{}: {}".format(tnum, n*i)
    