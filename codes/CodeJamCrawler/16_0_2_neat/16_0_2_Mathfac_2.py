import sys

def rev(k):
    for i in xrange(len(k)):
        k[i] = str((int(k[i]) + 1) % 2)[0]
    return k[::-1]
    

def solve(k):
    #print(k)
    if not len(k):
        return 0
    if k[-1] == "1":
        return solve(k[:-1])
    if k[-1] == "0":
        i=0
        while (k[i]=="1"):
            i+=1
            k[i] = "0"
        return (i > 0) + 1 + solve(rev(k)[:-1])

inp = sys.stdin.readlines()
tn = inp[0]
ti = 1
for k in inp[1:]:
    print("Case #{}: {}".format(ti,solve(list(k.replace("+", "1").replace("-", "0").strip())) ))
    ti += 1