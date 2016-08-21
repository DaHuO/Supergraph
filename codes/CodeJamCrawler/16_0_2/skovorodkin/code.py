import re

def rint():
    return int(rstr())

def rints(n):
    return [int(s) for s in rstrs(n)]

def rstr():
    return input()

def rstrs(n):
    return [rstr() for _ in range(n)]

def out(cases):
    for i, c in enumerate(cases, 1):
        print('Case #{}: {}'.format(i, solve(c)))


def solve(s):
    s = s[:s.rfind('-') + 1]
    return 0 if not s else len(re.findall('-+', s)) * 2 - (1 if s[0] == '-' else 0)


if __name__ == '__main__':
    T = rint()
    cases = rstrs(T)
    out(cases)

