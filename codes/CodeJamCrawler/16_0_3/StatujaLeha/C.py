from math import sqrt

def input(file):
    #F = open(file, "r")
    #T = int(F.readline())
    #for i in range(T):
    #    yield (i + 1), F.readline().strip()
    yield 1, (16, 50)
    #yield 1, (6, 3)

def toStr(n, base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

def firstDivisor(N):
    if 0 == N % 2: return 2

    for d in range(3, int(sqrt(N)) + 1, 2):
        if 0 == N % d: return d

    return -1

def solve(N, J):
    R = []
    for m in range(2**(N - 2) + 1):
        mStr = toStr(m, 2)
        mStr = ("0" * (N - 2 - len(mStr))) + mStr
        s = "1%s1" % mStr
        r = [firstDivisor(int(s, b)) for b in range(2, 10 + 1)]

        if -1 not in r: R.append((s, r))
        if J == len(R):
            return "\n".join([s + " " + " ".join([str(e) for e in r]) for (s, r) in R])

    return "!"

out = open("C.out", "w")

for (case, S) in input(""):
#for (case, S) in input("B-small-attempt0.in"):
#for (case, S) in input("B-large.in"):
    print("Case #%d:\n%s" % (case, solve(S[0], S[1])), file = out)
    #print("Case #%d:\n%s" % (case, solve(S[0], S[1])))
