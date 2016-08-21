from collections import defaultdict
import sys

words = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
wd = [defaultdict(int) for w in words]
for i in xrange(len(words)):
    w = words[i]
    for c in w:
        wd[i][c] += 1

def hasNumber(d, i):
    global words, wd
    w = words[i]
    for c in w:
        if d[c] < wd[i][c]:
            return False
    return True

def decNumber(d, i):
    global words, wd
    for c in words[i]:
        d[c] -= 1
        assert d[c] >= 0

TC = int(sys.stdin.readline())

# Returns (b, phone)
# b == True iff possible and phone when b == True
def solve(d, phone):
    if sum(d.values()) == 0:
        return True, phone
    for i in xrange(10):
        if hasNumber(d, i):
            dt = defaultdict(int)
            for x,y in d.items():
                dt[x] += y
            decNumber(dt, i)
            b, newPhone = solve(dt, phone + str(i))
            if b:
                return True, newPhone

    return False, ""

for tc in xrange(1,1+TC):
    l = sys.stdin.readline().strip()
    d = defaultdict(int)
    for c in l:
        d[c] += 1
    b, phone = solve(d, "")

    print "Case #%d: %s" % (tc, phone)
