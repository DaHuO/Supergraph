def solve(s):
    count = 0
    l = len(s)
    while l != s.count('+'):
        ch = s[0]
        i = 1
        while i < l:
            if s[i] != ch:
                break
            i += 1
        tmp = ''
        for j in xrange(i):
            if s[j] == '+':
                tmp += '-'
            else:
                tmp += '+'
        tmp += s[i:]
        s = tmp
        count += 1
    return count


if __name__ == '__main__':
    t = input()
    for i in xrange(1, t+1):
        s = raw_input().strip()
        print "Case #%d: %d" % (i, solve(s))