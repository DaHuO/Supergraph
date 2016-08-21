import sys

rd = open("B-large.in","r")
wrt = open("B.out", "w")

def fun(s):
    s = list(s)
    prev = s[0]
    cnt = 0
    if len(s) == s.count("+"):
        return 0
    if len(s) == s.count("-"):
        return 1
    for curr in s:
        if curr != prev:
            cnt += 1
        prev = curr
    if s.count("-")<len(s) and s[-1] == "-":
        cnt += 1
    return cnt

for test in xrange(1, int(rd.readline().strip()) + 1):
    n = fun(rd.readline().strip())
    ans = "Case #%d: %d\n" %(test,n)
    wrt.write(ans)

wrt.close()
