n = int(raw_input())
for c in range(n):
    arg = raw_input()
    case = '/'
    count = 0
    for cake in arg:
        if cake == case:
            continue;
        else:
            case = cake
            count += 1
    
    if arg[-1] == '+':
        count -= 1
    print "Case #%d: %d" % (c+1, count)
