from collections import Counter

digits = ["ZERO", "ONE", "TWO", "THREE", \
          "FOUR", "FIVE", "SIX", "SEVEN", \
          "EIGHT", "NINE"]

counts = [Counter(_) for _ in digits]

def getting_the_digits():
    def check(cnt, ans, i, l):
        if i == l:
            tmp = Counter()
            for _ in ans:
                tmp += Counter(digits[_])
            return tmp == cnt

        if i == 0:
            start = 0
        else:
            start = ans[i - 1]
        for d in xrange(start, 10):
            ans[i] = d
            if check(cnt, ans, i + 1, l):
                return True
        return False

    S = raw_input().strip()
    cnt = Counter(list(S))
    lower, upper = len(S) // 5, len(S) // 3
    for l in xrange(lower, upper + 1):
        ans = [0] * l
        if check(cnt, ans, 0, l):
            return "".join(map(str, ans))


for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, getting_the_digits())
