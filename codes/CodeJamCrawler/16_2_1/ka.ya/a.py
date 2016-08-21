def solve(s):
    count = [0] * 91
    for c in s:
        count[ord(c)] += 1
    digits = [0] * 10
    res = ''
    while count[ord('Z')] > 0:
        digits[0] += 1
        count[ord('Z')] -= 1
        count[ord('E')] -= 1
        count[ord('R')] -= 1
        count[ord('O')] -= 1
    while count[ord('W')] > 0:
        digits[2] += 1
        count[ord('T')] -= 1
        count[ord('W')] -= 1
        count[ord('O')] -= 1
    while count[ord('U')] > 0:
        digits[4] += 1
        count[ord('F')] -= 1
        count[ord('O')] -= 1
        count[ord('U')] -= 1
        count[ord('R')] -= 1
    while count[ord('F')] > 0:
        digits[5] += 1
        count[ord('F')] -= 1
        count[ord('I')] -= 1
        count[ord('V')] -= 1
        count[ord('E')] -= 1
    while count[ord('X')] > 0:
        digits[6] += 1
        count[ord('S')] -= 1
        count[ord('I')] -= 1
        count[ord('X')] -= 1
    while count[ord('V')] > 0:
        digits[7] += 1
        count[ord('S')] -= 1
        count[ord('E')] -= 2
        count[ord('V')] -= 1
        count[ord('N')] -= 1
    while count[ord('G')] > 0:
        digits[8] += 1
        count[ord('E')] -= 1
        count[ord('I')] -= 1
        count[ord('G')] -= 1
        count[ord('H')] -= 1
        count[ord('T')] -= 1
    while count[ord('O')] > 0:
        digits[1] += 1
        count[ord('O')] -= 1
        count[ord('N')] -= 1
        count[ord('E')] -= 1
    while count[ord('T')] > 0:
        digits[3] += 1
        count[ord('T')] -= 1
        count[ord('H')] -= 1
        count[ord('R')] -= 1
        count[ord('E')] -= 2
    while count[ord('N')] > 0:
        digits[9] += 1
        count[ord('N')] -= 2
        count[ord('I')] -= 1
        count[ord('E')] -= 1
    for c in range(ord('A'), ord('Z')+1):
        if count[c] > 0:
            print '!!!'
            exit()
    res = ''
    for i in range(10):
        while digits[i] > 0:
            res += str(i)
            digits[i] -= 1
    return res

t = input()
for i in xrange(1, t+1):
    s = raw_input()
    print 'Case #{}: {}'.format(i, solve(s))
