T = int(input())

def solution(s):
    res = 0
    s = list(s)
    while True:
        if '-' not in s:
            return res
        res += 1
        if s[0] == '-':
            if not s.count('+'):
                s = ['+'] * len(s)
            else:
                s = ['+'] * s.index('+') + s[s.index('+'):]
        else:
            s = ['-'] * s.index('-') + s[s.index('-'):]
    return res

for test in range(1, T + 1):
    s = input().strip()
    print("Case #{0}: {1}".format(test, solution(s)))
