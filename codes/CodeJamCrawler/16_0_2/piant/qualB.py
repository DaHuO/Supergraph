def pancakes(sides):
    i = 0
    current_side = sides[0]
    flips = 0
    # print sides
    while i < len(sides):
        while i < len(sides) and sides[i] == current_side:
            i += 1
        if i == len(sides):
            return flips + (current_side == '-')
        # print 'flip all before', i, 'to', sides[i]
        flips += 1
        current_side = sides[i]
        i += 1
    return flips + (current_side == '-')

t = int(raw_input())
for i in range(t):
    case = raw_input().strip()
    print 'Case #%d:' % (i+1), pancakes(case)
