__author__ = 'sumant'


def get_min_flips(pancake_str):
    if pancake_str == '':
        return 0
    num_flips = 0
    plus_seen = True if pancake_str[0] == '+' else False
    minus_seen = not plus_seen
    for i in range(1, len(pancake_str)):
        c = pancake_str[i]
        if c == '+' and minus_seen:
            num_flips += 1
            plus_seen = True
            minus_seen = False
        elif c == '-' and plus_seen:
            num_flips += 1
            plus_seen = False
            minus_seen = True
    if minus_seen:
        num_flips += 1
    return num_flips


if __name__ == '__main__':
    n = int(raw_input())
    for i in range(n):
        s = str(raw_input())
        print 'Case #%s: %s' % (i+1, get_min_flips(s))