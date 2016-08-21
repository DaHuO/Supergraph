def take(digit, letters):
    need = RULES[digit]
    cnt = 4000
    for k, v in need.iteritems():
        v2 = letters.get(k, 0)
        if v2 < v:
            return 0
        cnt = min(cnt, v2 // v)

    cnt = 1
    for k, v in need.iteritems():
        letters[k] -= (v * cnt)
        if not letters[k]:
            del letters[k]
    return cnt


def put_back(digit, letters, cnt):
    need = RULES[digit]
    for k, v in need.iteritems():
        letters.setdefault(k, 0)
        letters[k] += (v * cnt)


def find(digit, letters, path):
    if not letters:
        return list(path)

    for shift in xrange(10):
        digit_next = digit + shift
        if digit_next <= 9:
            cnt = take(digit_next, letters)
            if cnt > 0:
                res = find(digit_next, letters, path + [digit_next,] * cnt)
                if res:
                    return res
                put_back(digit_next, letters, cnt)


def compress(S):
    l = {}
    for c in S:
        l.setdefault(c, 0)
        l[c] += 1
    return l


def solve(S):
    letters = compress(S)
    for i in xrange(10):
        digits = find(i, letters, [])
        if digits:
            return ''.join(map(lambda x: chr(x + ord('0')), digits))


RULES = map(compress, ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR',
                       'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE'])

T = int(raw_input())

for i in xrange(T):
    i += 1
    S = raw_input().strip()
    print 'Case #{0}:'.format(i), solve(S)
