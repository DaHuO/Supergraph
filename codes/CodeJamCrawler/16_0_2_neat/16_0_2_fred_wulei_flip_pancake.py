def flip(pancake):
    pancake = pancake.rstrip("+")
    if not pancake:
        return 0

    last = pancake[0]
    shift = 0

    for p in pancake[1:]:
        if p == last:
            continue
        else:
            shift += 1
            last = p
    if last == '-':
        shift += 1
    
    return shift

def solve(file):
    f = open(file, 'r')
    count = f.readline()
    case = 1
    for l in f.readlines():
        pancake = l.strip()
        print 'Case #%d: %s' % (case, flip(pancake))
        case += 1
    f.close()

solve('B-large.in')





