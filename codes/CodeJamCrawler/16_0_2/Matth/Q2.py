fin = open("in.in")
fout = open("out.out","w")
data = fin.read().split("\n")
T = int(data.pop(0))
fin.close()
for i in range(1, T+1):
    s = data[i-1]
    cnt = 1
    for j in range(1, len(s)):
        if s[j]!=s[j-1]: cnt += 1
    if s[len(s)-1] == "+": cnt -= 1
    print >>fout, "Case #%d: %d" % (i, cnt)
fout.close()