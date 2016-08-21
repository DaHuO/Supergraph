import sys
def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

def flip(N, X):
	orgN = list(N)
	if X == 1:
		N[0] = '+' if N[0] == '-' else '-'
	else:
		for i in range(0, X/2):
			if i == 0 and N[i] == ('+' if N[X-i - 1] == '-' else '-'):
				return flip(N, X-1)

			temp = N[i]
			N[i] = '+' if N[X-i - 1] == '-' else '-'
			N[X-i - 1] = '+' if temp == '-' else '-'
	
		if X % 2 == 1:
			N[X/2] = '+' if N[X/2] == '-' else '-'
	if orgN == N:
		return flip(N, X-1)
	return N

def findIt(N):
	if set(N) == set(['+','+','+']):
		return 0
	else:
		for x in range(len(N) - 1, -1, -1):
			if N[x] == '-':
				N = flip(N, x + 1)
				print "NEXT"
				print N
				print x + 1
				return findIt(N) + 1

results = []
firstLine = True
with open("B-large.in") as f:
	contents = f.readlines()
	for content in contents:
		if not firstLine:
			results.append(findIt(list(content.strip("\n"))))
		firstLine = False;
	f.close()

file = open("a.out", "w")
counter = 1
for item in results:
	file.write("Case #" + str(counter) + ": " + str(item) + "\n")
	counter += 1

file.close()