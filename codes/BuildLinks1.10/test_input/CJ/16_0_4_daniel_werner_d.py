import math


def solve(k, c, s):

 tries = int(math.ceil(k / float(c)))
 if s < tries:
  return "IMPOSSIBLE"
 
 indexes = []
 curK = 0
 for i in range(0, tries):
  ind = 0
  mult = k**(c-1)
  for j in range(0, c):
   ind += curK * mult
   mult /= k
   curK += 1
   if curK >= k:
    break
  oldInd = ind
  ind = min(ind, k**c - 1)
  if oldInd != ind:
   print "##############" + str(oldInd - ind) + "############"
  indexes.append(str(ind + 1))
  
 return " ".join(indexes)


name = "storage/emulated/0/codejam/D-large"
fi = open(name + ".in", "r")

fout = open(name + ".out", "w")

numTestCases = int(fi.readline())
print "#TestCases: ", numTestCases

for i in range(0, numTestCases):
 line = fi.readline().strip().split(" ")
 line = map(int, line)
 k = line[0]
 c = line[1]
 s = line[2]

 fout.write("Case #" + str(i + 1) + ": " + solve(k, c, s) + "\n")
 print "Case #" + str(i + 1) + ": " + solve(k, c, s)

fi.close()
fout.close()