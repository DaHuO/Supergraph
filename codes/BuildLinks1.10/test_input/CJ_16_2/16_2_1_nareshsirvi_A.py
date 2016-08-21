
def rec(SD, out):
    if len(SD) == 0:
        return out

    for ds, d in (("ZERO", "0"), ("ONE", "1"), ("TWO", "2"), ("THREE", "3"), 
            ("FOUR", "4"), ("FIVE", "5"), ("SIX", "6"), ("SEVEN", "7"), 
            ("EIGHT", "8"), ("NINE", "9")):
        rem = []
        for c in ds:
            if SD.get(c, 0) <= 0:
                break
            SD[c] = SD[c] - 1
            if SD.get(c, 0) == 0:
                del SD[c]
            rem.append(c)
        else:
            out.append(d)
            tmp = rec(SD, out)
            if tmp:
                return tmp
            out.remove(d)

        for c in rem:
            SD[c] = SD.get(c, 0) + 1


if __name__ == "__main__":
    T = input()
    for i in range(1, T + 1):
        S = raw_input()
        SD = {}
        for c in S:
            SD[c] = SD.get(c, 0) + 1
        out = []
        res = rec(SD, out)
        res.sort()

        print 'Case #%d: %s' % (i, ''.join(res))

