import sys

def flip(c):
    if c == '+':
        return '-'
    else:
        return '+'

def calculate(s):
    cur_target = '+'
    cur_p = len(s) - 1
    ans = 0
    while cur_p >= 0:
        if s[cur_p] == cur_target:
            cur_p -= 1
            continue
        ans += 1
        if s[0] == s[cur_p]:
            for i in range(0, cur_p / 2 + 1):
                s[i], s[cur_p - i] = flip(s[cur_p - i]), flip(s[i])
        else:
            cur_target = flip(cur_target)
        cur_p -= 1
    return ans

input_file = sys.argv[1]
with open(input_file, 'r') as f:
    t = int(f.readline())
    for i in range(0, t):
        s = f.readline().strip()
        print('Case #%d: %s' % ((i + 1), str(calculate(list(s)))))
