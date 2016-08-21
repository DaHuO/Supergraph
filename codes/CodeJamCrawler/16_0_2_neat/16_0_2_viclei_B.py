fName = 'B-large.in'
lines = open(fName, 'r')
out = open('out.txt', 'w')

N = int(lines.next())
for t in xrange(1, N+1):
    stack = str(lines.next()).strip()
    print stack, len(stack)
    s_len = len(stack)
    # target = str('+', s_len)
    moves = 0
    i = 0
    while i < s_len:
        if stack[i] == '+':
            i += 1
            continue
        else:
            # Flip the + on top
            if i > 0:
                moves += 1

            # and then flip it all into +
            moves += 1
            while i < s_len and stack[i] == '-':
                i += 1

    out.write('Case #%i: %i\n'%(t, moves))





