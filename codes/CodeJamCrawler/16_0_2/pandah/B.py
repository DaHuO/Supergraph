def main(T, S):
    m = {"+": 1, "-": 0}
    bitstr = map(lambda x: m[x], S)
    f = 0
    res = 0
    while f < len(bitstr):
        while f < len(S) and bitstr[f] == 1:
            f += 1
        if f >= len(bitstr):
            break
        for q in xrange(f, len(bitstr)):
            if bitstr[q] == 1:
                bitstr[q] = 0
            else:
                bitstr[q] = 1
        res += 1
    print "Case #%s: %d" % (T, res)

if __name__ == "__main__":
    T = int(raw_input()) 
    for t in xrange(1, T+1):
        main(t, raw_input()[::-1])
