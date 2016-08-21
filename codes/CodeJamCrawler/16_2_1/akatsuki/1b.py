def magic():
    t = input()
    for tc in xrange(t):
        freq = [0]*256
        s = raw_input()
        for i in s:
            freq[ord(i)] += 1

        res = []
        if freq[ord('Z')] > 0:
            c = freq[ord('Z')]
            freq[ord('Z')] -= c
            freq[ord('E')] -= c
            freq[ord('R')] -= c
            freq[ord('O')] -= c
            while c > 0:
                res.append('0')
                c -= 1
        if freq[ord('G')] > 0:
            c = freq[ord('G')]
            freq[ord('E')] -= c
            freq[ord('I')] -= c
            freq[ord('G')] -= c
            freq[ord('H')] -= c
            freq[ord('T')] -= c
            while c > 0:
                res.append('8')
                c -= 1
        if freq[ord('X')] > 0:
            c = freq[ord('X')]
            freq[ord('S')] -= c
            freq[ord('I')] -= c
            freq[ord('X')] -= c
            while c > 0:
                res.append('6')
                c -= 1
        if freq[ord('S')] > 0:
            c = freq[ord('S')]
            freq[ord('S')] -= c
            freq[ord('E')] -= c
            freq[ord('V')] -= c
            freq[ord('E')] -= c
            freq[ord('N')] -= c
            while c > 0:
                res.append('7')
                c -= 1
        if freq[ord('V')] > 0:
            c = freq[ord('V')]
            freq[ord('F')] -= c
            freq[ord('I')] -= c
            freq[ord('V')] -= c
            freq[ord('E')] -= c
            while c > 0:
                res.append('5')
                c -= 1
        if freq[ord('F')] > 0:
            c = freq[ord('F')]
            freq[ord('F')] -= c
            freq[ord('O')] -= c
            freq[ord('U')] -= c
            freq[ord('R')] -= c
            while c > 0:
                res.append('4')
                c -= 1
        if freq[ord('H')] > 0:
            c = freq[ord('H')]
            freq[ord('T')] -= c
            freq[ord('R')] -= c
            freq[ord('H')] -= c
            freq[ord('E')] -= c
            freq[ord('E')] -= c
            while c > 0:
                res.append('3')
                c -= 1
        if freq[ord('W')] > 0:
            c = freq[ord('W')]
            freq[ord('T')] -= c
            freq[ord('W')] -= c
            freq[ord('O')] -= c
            while c > 0:
                res.append('2')
                c -= 1
        if freq[ord('O')] > 0:
            c = freq[ord('O')]
            freq[ord('O')] -= c
            freq[ord('N')] -= c
            freq[ord('E')] -= c
            while c > 0:
                res.append('1')
                c -= 1
        if freq[ord('I')] > 0:
            c = freq[ord('I')]
            freq[ord('N')] -= c
            freq[ord('I')] -= c
            freq[ord('N')] -= c
            freq[ord('E')] -= c
            while c > 0:
                res.append('9')
                c -= 1
        res.sort()
        print "Case #%d: %s" % (tc+1, ''.join(res))
magic()