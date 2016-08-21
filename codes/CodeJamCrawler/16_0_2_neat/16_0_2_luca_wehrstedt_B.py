def solve(s):
    if not "-" in s:
        return 0
    if not "+" in s:
        return 1
    cnt = 0
    while "-" in s:
        if s[0] == '+':
            idx = s.index('-')
            s = idx * "-" + s[idx:]
            #print(s)
            cnt += 1
        else:
            idx = s.rindex('-') + 1
            s = "".join({"+":"-", "-":"+"}[i] for i in s[:idx]) + s[idx:]
            #print(s)
            cnt += 1
    return cnt


t = int(input())
for i in range(t):
    s = input().strip()
    print("Case #%d: %d" % (i+1, solve(s)))
