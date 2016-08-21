import sys

def highest(remaining):
    for i in range(25, -1, -1):
        if remaining[i] > 0:
            return chr(ord('A') + i)


def genword(ret, word, used):
    if len(word) == 0:
        return ret
    used[ord(word[0]) - ord('A')] += 1
    if highest(used) <= word[0]:
        return genword(word[0] + ret, word[1:], used)
    else:
        return genword(ret + word[0], word[1:], used)


def solve(word):
    used = [0] * 26
    used[ord(word[0]) - ord('A')] += 1
    return genword(word[0], word[1:], used)


sys.setrecursionlimit(10000)
cases = int(raw_input())
for case in xrange(cases):
    word = raw_input()
    print "Case #%d:" % (case + 1), solve(word)
