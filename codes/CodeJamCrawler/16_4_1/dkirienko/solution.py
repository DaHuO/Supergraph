def ans(p, r, s):
    n = p + r + s
    if n == 1:
        return "P" * p + "R" * r + "S" * s
    nn = n // 2
    p1 = p // 2
    r1 = r // 2
    s1 = s // 2
    n1 = p1 + r1 + s1
    if p1 * 2 < p and n1 < n // 2:
        p1 += 1
        n1 += 1
    if r1 * 2 < r and n1 < n // 2:
        r1 += 1
        n1 += 1
    if s1 * 2 < s and n1 < n // 2:
        s1 += 1
        n1 += 1
    p2 = p - p1
    r2 = r - r1
    s2 = s - s1
    return ans(p1, r1, s1) + ans(p2, r2, s2)

def solve():
    n, r, p, s = map(int, input().split())
    if abs (r - p) > 1 or abs(p - s) > 1 or abs(r - s) > 1:
        return "IMPOSSIBLE"
    else:
        return ans(p, r, s)

for i in range(1, int(input()) + 1):
    print("Case #", i, ": ", solve(), sep="")

