# K = 1
# Check S = 1
# 1,1,1
#
# K = 2
# AA
# aAaa
# 1,2
#
# K = 3
# AAA
# aAa aaa aAa
# aaa aaA ...
# 1,2,6
#
# K = 4
# AAAA
# aAaa aaaa aaaA aaaa
# aaaa aaAa ...
# 1,2,7,28
#
# K = 5
# AAAAA
# aAaaa...
# aaaaa aaAaa...
#
# 1,2,8,39

f = open('D-small-attempt1.in')
N = int(f.readline())
f1 = open('D-small-attempt1.out', 'wc')
def check_at(c,k):
    pt = min(c,k)
    if pt == 1:
        return 1
    prev = check_at(c-1,k)
    return (prev-1)*k + pt

for i in range(N):
    K, C, S = [int(x) for x in f.readline().split()]
    f1.write("Case #%i: " % (i+1))
    if C * S < K:
        f1.write("IMPOSSIBLE\n")
        continue

    check_pt = check_at(C,K)
    checks = []
    for _ in range(S):
        checks.append(check_pt)
        check_pt = check_pt + K ** (C-1)
        if check_pt > K ** C:
            break
    f1.write(" ".join([str(x) for x in checks]))
    f1.write("\n")
