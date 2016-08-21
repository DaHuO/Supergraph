import sys

digits = "0123456789"
def dfs(C, J, a, b):
    # print >> sys.stderr, a, b
    if not C and not J:
        return abs(int(a) - int(b)), a, b
    c0, j0 = C[0], J[0]
    xx = digits if c0 == '?' else c0
    yy = digits if j0 == '?' else j0
    diff = sorted([(abs(int(a + x) - int(b + y)), a + x, b + y) for x in xx for y in yy])
    return min(dfs(C[1:], J[1:], ax, by) for d, ax, by in diff if d <= diff[0][0] + 1)


def main():
    T = int(sys.stdin.readline())
    for t in range(1, T+1):
        C, J = sys.stdin.readline().split()
        # print >> sys.stderr, "C", C, "J", J
        _, c, j = dfs(C, J, "", "")
        print "Case #%d:" % t, c, j

if __name__ == "__main__":
    main()
