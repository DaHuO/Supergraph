import sys
sys.stdout = open("out.txt", "w")


def remdup(s):
    t = []
    t.append(s[0])
    for i in range(1, len(s)):
        if t[-1] != s[i]:
            t.append(s[i])
    return ''.join(t)


def flip(s):
    t = []
    for c in s:
        if c == '+':
            t.append('-')
        else:
            t.append('+')
    t.reverse()
    return ''.join(t)


def solve(s):
    ans = 0
    while s.find('-') != -1:
        #print("s: {}".format(s))
        ans = ans + 1
        r = s.rfind('-')
        if s[0] == '+':
            s = flip(s[:r]) + s[r:]
        else:
            s = flip(s[:r+1]) + s[r+1:]
    return ans

lines = []

with open("B-large.in", "r") as f:
    lines = f.readlines()

n = int(lines[0])

for i in range(1, n+1):
    change = remdup(lines[i].strip())
    ans = solve(change)
    print("Case #{}: {}".format(i, str(ans)))
