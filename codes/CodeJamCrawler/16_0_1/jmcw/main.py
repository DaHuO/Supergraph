
from sets import Set

t = int(raw_input())

for i in range(t):
    
    print "Case #{}:".format(i+1),

    s = int(raw_input())

    unseen = Set(range(0,10))

    i = 1

    if s == 0:
        print "INSOMNIA"
    else:

        while len(unseen) > 0:
            v = s * i
            for c in [int(x) for x in str(v)]:
                if c in unseen: unseen.remove(c)
            i += 1

        print v

