import sys


def lastword(word):
    res = word[0]
    for char in word[1::]:
        if char >= res[0]:
            res = char + res
        else:
            res = res + char
    return res

n_cases = int(sys.stdin.readline())

for i in range(n_cases):
    word = sys.stdin.readline().strip()
    print 'Case #' + str(i + 1) + ":", lastword(word)