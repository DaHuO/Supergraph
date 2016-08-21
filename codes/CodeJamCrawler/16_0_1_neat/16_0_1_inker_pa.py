for case in range(1, int(raw_input())+1):
    print "Case #%d: "%case, 
    n = int(raw_input())
    if n == 0:
        print "INSOMNIA"
        continue
    s = set()
    nn = 0
    while len(s) != 10:
        nn += n
        s |= set(str(nn))
    print nn
