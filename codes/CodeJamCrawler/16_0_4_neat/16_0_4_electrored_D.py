import sys

rd = open("D-small-attempt0.in","r")
wrt = open("D.out", "w")

for test in xrange(1, int(rd.readline().strip()) + 1):
    k,c,s = map(int,rd.readline().strip().split())
    ans = range(1,k+1)
    ans = " ".join(str(i) for i in ans)
    ansf = "Case #%d: %s\n" %(test,ans)
    wrt.write(ansf)

wrt.close()
