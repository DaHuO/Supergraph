
def sol():
    s = input()
    a = ""
    for i, c in enumerate(s):
        if len(a) < 1 or c >= a[0]:
            a = c + a
        else:
            a = a + c
    return a

t = int(input())
for i in range(t):
    print("Case #%s: %s" % (i+1, sol()))
