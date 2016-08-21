def reverse(sign):
    return '-' if sign == '+' else '+'


def compute(s, expected_sign):
    if len(s) == 0:
        return 0
    if s[-1] == expected_sign:
        return compute(s[0: -1], expected_sign)
    else:
        return 1 + compute(s[0: -1], reverse(expected_sign))


t = int(raw_input())
for i in range(1, t + 1):
    s = raw_input()
    print "Case #{}: {}".format(i, compute(s, '+'))
