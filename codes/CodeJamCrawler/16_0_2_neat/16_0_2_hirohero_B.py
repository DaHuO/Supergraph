a = open('B-large.in','r').readlines()
f = open('B-large.out','w')


def solve(s):
    now = 0
    s = s[::-1]
    for i in range(len(s)):
        if ((s[i] == '+') & (now % 2 == 1)) | ((s[i] == '-') & (now % 2 == 0)):
            now += 1
    return str(now)
for test in range(1, int(a[0].strip()) + 1):
    print >> f, "Case #" + str(test) + ': ' + solve(a[test].strip())

f.close()
