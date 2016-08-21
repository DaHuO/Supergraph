from collections import defaultdict
nos = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
S = defaultdict(int)

def remove_no(ct, val=1):
    for c in nos[ct]:
        S[c] -= val

n = int(input())
for _ in xrange(1, n+1):
    a = raw_input()
    ans = []
    S = defaultdict(int)
    for ch in a:
        S[ch] += 1
    #for eight
    for no, ch in [(0, 'Z'), (2, 'W'), (4, 'U'), (3, 'R'), (6, 'X'), (8, 'G'), (5, 'F'), (7, 'V'), (9, 'I'), (1, 'N')]:
        ans.extend([no]*S[ch])
        remove_no(no, S[ch])
    ans.sort()
    print "Case #%d: %s" % (_, "".join(map(str, ans)))
