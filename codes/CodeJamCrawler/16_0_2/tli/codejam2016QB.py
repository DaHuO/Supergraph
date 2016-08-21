t = input()

for i in xrange(t):
    s = raw_input()
    num_inversions = 0

    cur_char = s[0]

    for j in xrange(1, len(s)):
        if cur_char != s[j]:
            num_inversions += 1
            cur_char = s[j]

    parity = 0 if s[0] == '+' else 1
    parity += num_inversions

    c = num_inversions + parity % 2
    print "Case #" + str(i + 1) + ": " + str(c)
