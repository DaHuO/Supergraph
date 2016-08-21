# Greedily choose the first viable solution - try paper then rock then scissors, to put things in alphabetical order
def drawing(l):
    # print("Checking whether", l, "is drawing...")
    if len(l) < 2:
        return False
    s = ""
    for i in range(0, len(l) + 1, 2):
        p = l[i:i+2]
        # print("Slice:", p)
        if p in ("PP", "RR", "SS"):
            return True
        if p in ("PR", "RP"):
            s += "P"
        if p in ("PS", "SP"):
            s += "S"
        if p in ("RS", "SR"):
            s += "R"
    return drawing(s)
for t in range(int(input())):
    n, r, p, s = map(int, input().split())
    # print("Finding solution with:", n, p, r, s)
    def step(l, n, p, r, s):
        if p < 0 or r < 0 or s < 0:
            return False
        if drawing(l):
            # print("Drawing; backtracking")
            return False
        if n == 0:
            return l
        res = step(l + "P", n - 1, p - 1, r, s)
        if res:
            return res
        res = step(l + "R", n - 1, p, r - 1, s)
        if res:
            return res
        res = step(l + "S", n - 1, p, r, s - 1)
        if res:
            return res
        # print("Possibilities exhausted; backtracking")
        return False
    print("Case #%d: %s" % (t + 1, step("", 2 ** n, p, r, s) or "IMPOSSIBLE"))