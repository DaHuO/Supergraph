def solve(s):
    last_word = ''
    for c in s:
        p1 = last_word + c
        p2 = c + last_word
        last_word = max(p1, p2)
    return last_word,


def read_input():
    s = raw_input().strip()
    return s,

if __name__ == '__main__':
    t = int(raw_input())
    for i in range(t):
        res = map(str, solve(*read_input()))
        print "Case #%s: %s" % ( i+1, " ".join(res) )

    # test_cases = [
    #     ('CAB', ),
    #     ('JAM', ),
    #     ('CODE', ),
    #     ('ABAAB', ),
    #     ('CABCBBABC', ),
    #     ('ABCABCABC', ),
    #     ('ZXCASDQWE', ),
    # ]
    # for i, test in enumerate(test_cases):
    #     res = map(str, solve(*test))
    #     print "Case #%s: %s" % ( i+1, " ".join(res) )