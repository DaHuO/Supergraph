inp = open('getting-the-digits-large.in', 'r')
raw_input = inp.readline
T = int(raw_input())
out = open('getting-the-digits-large.out', 'w')

for t in xrange(T):
    oword = raw_input().strip()
    word = list(oword)
    counts = [0] * 10
    try:
        z = word.count('Z')
        counts[0] = z
        for y in xrange(z):
            for c in 'ZERO':
                word.remove(c)
        z = word.count('W')
        counts[2] = z
        for y in xrange(z):
            for c in 'TWO':
                word.remove(c)
        z = word.count('U')
        counts[4] = z
        for y in xrange(z):
            for c in 'FOUR':
                word.remove(c)
        z = word.count('X')
        counts[6] = z
        for y in xrange(z):
            for c in 'SIX':
                word.remove(c)
        z = word.count('G')
        counts[8] = z
        for y in xrange(z):
            for c in 'EIGHT':
                word.remove(c)
        z = word.count('O')
        counts[1] = z
        for y in xrange(z):
            for c in 'ONE':
                word.remove(c)
        z = word.count('T')
        counts[3] = z
        for y in xrange(z):
            for c in 'THREE':
                word.remove(c)
        z = word.count('F')
        counts[5] = z
        for y in xrange(z):
            for c in 'FIVE':
                word.remove(c)
        z = word.count('V')
        counts[7] = z
        for y in xrange(z):
            for c in 'SEVEN':
                word.remove(c)
        z = word.count('E')
        counts[9] = z
        for y in xrange(z):
            for c in 'NINE':
                word.remove(c)
    except:
        print oword
        raise
    count = [str(k) * counts[k] for k in range(10)]
    out.write("Case #" + str(t + 1) + ": " + ''.join(count) + "\n")

out.close()
