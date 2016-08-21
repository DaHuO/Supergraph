def close_match():
    def match(s1, s2):
        if len(s1) != len(s2):
            return False
        for i in xrange(len(s1)):
            if s2[i] != '?' and s1[i] != s2[i]:
                 return False
        return True
    S, J = raw_input().strip().split()
    Ss = [str(i).zfill(len(S)) for i in xrange(1000) if match(str(i).zfill(len(S)), S)]
    Js = [str(i).zfill(len(J)) for i in xrange(1000) if match(str(i).zfill(len(J)), J)]
    res = ("1000", "1000")
    min_diff = 1000
    for i in Ss:
        for j in Js:
            if abs(int(i) - int(j)) < min_diff or \
               (abs(int(i) - int(j)) == min_diff and \
               int(i) + int(j) <= int(res[0]) + int(res[1])):
                min_diff = abs(int(i) - int(j))
                res = (i, j)
    return res

for case in xrange(input()):
    S, J = close_match()
    print 'Case #%d: %s %s' % (case+1, S, J)