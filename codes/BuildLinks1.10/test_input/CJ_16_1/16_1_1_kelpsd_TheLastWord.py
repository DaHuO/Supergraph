import sys

def last_words_rec(s, base):

    if len(s) == 1:
        result = [s+base] + [base+s]

    else:
        result = last_words_rec(s[1:], s[0]+base) + last_words_rec(s[1:], base+s[0])

    return result


def alphLast(words):
    words.sort()
    return words[len(words)-1]


assert last_words_rec("a", "") == ["a", "a"]
# print(alphLast(last_words_rec("cab", "")))


t = int(sys.stdin.readline())

for i in range(0, t):
    s = sys.stdin.readline()
    print("Case #%d: %s" % (i+1, alphLast(last_words_rec(s, ""))))
