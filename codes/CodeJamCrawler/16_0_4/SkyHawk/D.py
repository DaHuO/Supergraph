import sys

T = int(raw_input())
for case_idx in xrange(1, T+1):
    sys.stdout.write("Case #{}: ".format(case_idx))
    k,c,s = map(int, raw_input().split())
    n_students = ((k + c - 1) / c)
    if s < n_students:
        print "IMPOSSIBLE"
        continue
    print " ".join([str(a + 1) for a in range(k)])

