t = int(raw_input())  # read a line with a single integer 
for c in xrange(1, t+1):
    N = int(raw_input())
    if N == 0:
        out = "INSOMNIA"
    else:
        reminder = [i for i in range(10)]
        out = 0
        while (len(reminder) > 0):
            out = out + N
            reminder = [x for x in reminder if x not in map(int, list(str(out)))]
    print "Case #{}: {}".format(c,out)
        
