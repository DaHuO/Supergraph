import sys

__author__ = 'PC'

def output(out, tc, res):
    out.write("Case #%s: %s\n" % (tc, res))

def flip(S):
    S = list(S)
    for i in range(len(S)):
        if S[i] == '-':
            S[i] = '+'
        else:
            S[i] = '-'
    return "".join(S)

with open('output', 'w+') as out:
    with open('input', 'r') as f:
        T = int(f.readline())
        for tc in range(1, T + 1):
            S = f.readline()

            count = 0
            for i in range(len(S) - 1, -1, -1):
                if S[i] == '-':
                    count += 1
                    S = flip(S)

            output(out, tc, str(count))
