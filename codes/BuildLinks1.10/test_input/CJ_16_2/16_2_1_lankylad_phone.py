if __name__ == '__main__':
    N = int(raw_input())
    for t in xrange(1,N+1):
        s = raw_input().strip()
        numbers = []
        inst = s.count('Z')
        for c in "ZERO":
            s = s.replace(c,'', inst)
        numbers += [0]*inst
        inst = s.count('W')
        for c in "TWO":
            s = s.replace(c,'', inst)
        numbers += [2]*inst
        inst = s.count('U')
        for c in "FOUR":
            s = s.replace(c,'', inst)
        numbers += [4]*inst
        inst = s.count('X')
        for c in "SIX":
           s = s.replace(c, '', inst)
        numbers += [6] * inst
        inst = s.count('G')
        for c in "EIGHT":
           s = s.replace(c, '', inst)
        numbers += [8] * inst
        inst = s.count('F')
        for c in "FIVE":
           s = s.replace(c, '', inst)
        numbers += [5] * inst
        inst = s.count('V')
        for c in "SEVEN":
           s = s.replace(c, '', inst)
        numbers += [7] * inst
        inst = s.count('R')
        for c in "THREE":
           s = s.replace(c, '', inst)
        numbers += [3] * inst
        inst = s.count('I')
        for c in "NINE":
           s = s.replace(c, '', inst)
        numbers += [9] * inst
        inst = s.count('N')
        for c in "ONE":
           s = s.replace(c, '', inst)
        numbers += [1] * inst

        numbers = sorted(numbers)
        print "Case #{}: {}".format(t, ''.join(str(x) for x in numbers))


