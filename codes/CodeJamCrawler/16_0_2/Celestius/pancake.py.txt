def pancake(s):
    last_blank = 1 if s[-1] == '-' else 0
    num_flips = 0
    prev = s[0]
    for char in s:
        if char != prev:
            num_flips += 1
            prev = char
    return num_flips + last_blank

t = int(raw_input())
for i in xrange(1, t+1):
    s = raw_input()
    print "Case #{0}: {1}".format(i, pancake(s))