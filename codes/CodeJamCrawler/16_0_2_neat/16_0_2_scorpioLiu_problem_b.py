import sys

sys.stdin = open('B-large.in.txt', 'r')
sys.stdout = open('b-large.out', 'w')


def reverse(data):
    data = data[::-1]
    return ''.join(['-' if s == '+' else '+' for s in data])


def find_diff(data):
    for i in range(len(data) - 1, 0, -1):
        if data[i] != data[i - 1]:
            return i
    return -1


def solution(data, tar='+'):
    if len(data) == 1 and data != tar:
        return 1
    r = 0
    i = find_diff(data)
    if data[i] != tar:
        r += 1
        tar = '+' if tar == '-' else '-'
    if i < 0:
        return r
    raw = data[:i]
    if raw[0] == raw[-1]:
        raw = reverse(raw)
        r = r + 1 + solution(raw, tar)
    else:
        r += 1
        idx = find_diff(raw)
        raw = raw[:idx]
        r = r + 1 + solution(raw, tar)
    return r


for t in range(int(input())):
    i = raw_input()
    r = solution(i)
    print 'Case #%d: %d' % (t + 1, r)
