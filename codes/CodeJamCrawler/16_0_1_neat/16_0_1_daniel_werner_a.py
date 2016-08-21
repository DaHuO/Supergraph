import math


def solve(n):
 
 if n == 0:
  return "INSOMNIA"
  
 seen = set()
 for i in range(1, 100):
  newn = str(i * n)
  for char in newn:
   seen.add(char)
  
  if len(seen) == 10:
   return newn 

 return "INSOMNIA"


name = "storage/emulated/0/codejam/A-large"
fi = open(name + ".in", "r")

fout = open(name + ".out", "w")

numTestCases = int(fi.readline())
print "#TestCases: ", numTestCases

for i in range(0, numTestCases):
	line = fi.readline().strip().split(" ")
	line = map(int, line)[0]

	fout.write("Case #" + str(i + 1) + ": " + solve(line) + "\n")
	print "Case #" + str(i + 1) + ": " + solve(line)

fi.close()
fout.close()