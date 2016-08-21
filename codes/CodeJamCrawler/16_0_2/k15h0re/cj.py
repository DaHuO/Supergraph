import re

transform = lambda line: re.sub(r'(\W)(?=\1)', '', line)
interchange = {'-': '+', '+': '-'}


def find_flips(s, prev):
    if s == '-':
        return 1
    if s == '+':
        return 0
    return find_flips(transform(interchange[s[:1]] + s[1:]), prev + 1) + 1


cases = int(raw_input())
for i in xrange(cases):
    print "Case #{}: {}".format(i + 1, find_flips(transform(raw_input()), 0))
