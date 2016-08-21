def num_flips(s):
    r = 1
    p = s[0]
    for i in range(1, len(s)):
        if p != s[i]: 
            r += 1
            p = s[i]
    return (s[0] == '+', r)

def f(i):
    s, r = num_flips(i)
    return (s == (r % 2 == 0)) + (r-1)

t = input()
import fileinput
numbers = map(lambda s: s[:-1],fileinput.input())[:t]

template = "Case #%d: %s"
for (i, r) in enumerate(map(f, numbers)):
    print(template % (i + 1,r))



