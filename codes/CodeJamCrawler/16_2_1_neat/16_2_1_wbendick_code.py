from collections import defaultdict

order = [0, 2, 6, 8, 4, 3, 5, 7, 1, 9]
critical = ['Z', 'W', 'X', 'G', 'U', 'T', 'F', 'S', 'O', 'I']
spellings = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]


def solve(word):
    out = ""
    l = [[x, word.count(x)] for x in set(word)]
    c = defaultdict(int)
    for k, v in l:
        c[k] += v

    for i in xrange(10):
        for j in xrange(c[critical[i]]):
            out = out + str(order[i])
            for letter in spellings[order[i]]:
                c[letter] -= 1
    return ''.join(sorted(list(out)))


cases = int(raw_input())
for case in xrange(cases):
    word = raw_input()
    print "Case #%d:" % (case + 1), solve(word)
