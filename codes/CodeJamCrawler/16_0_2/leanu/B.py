def flips(s):
    n=0
    if s[0]=='-':
        n=1
    n+=s.count('+-')*2
    return n

f = open('input.in', 'r')
T = int(f.readline())
tcs = []

for i in range(T):
    tcs.append(f.readline())

f.close()
f = open('output.txt', 'w')
for i in range(T):
    f.write("Case #%s: %s\n" % (i+1, flips(tcs[i])))
f.close()


