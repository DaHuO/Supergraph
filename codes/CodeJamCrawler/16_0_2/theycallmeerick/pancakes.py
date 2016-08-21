t = int(raw_input().strip())

def flip(st, j):
    s = ''
    for x in xrange(len(st)):
        if x <= j:
            if st[x] == '-':
                s += '+'
            else:
                s += '-'
        else:
            s += st[x]
    return s

def won(st):
    for x in st:
        if x == '-':
            return False
    return True

def findOptimal(st):

    s = ''
    for idx, x in enumerate(st):
        if x == '+' and len(s) > 0 and s[-1] == '-':
            return idx - 1
        s += x
    return len(st) - 1

def countN(st):
    moves = 0
    for y in xrange(len(st)):
        for x in xrange(len(st)):
            if won(st):
                return moves
            st = flip(st, findOptimal(st))
            moves += 1
    return moves
        
for _ in xrange(t):
    st = raw_input().strip()

    print 'Case #%d: %d' % (_ + 1, countN(st))
