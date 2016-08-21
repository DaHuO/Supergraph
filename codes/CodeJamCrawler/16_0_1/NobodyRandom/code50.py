def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

def findIt(N):
	found = []
	done = ['0','1','2','3','4','5','6','7','8','9']
	first = True
	X = 1
	for X in range(1, 1000001):
		num = list(str(X * int(N)))
		for Y in num:
			if first:
				found.append(Y)
				first = False
			foundInList = False
			for Z in found:
				if Z == Y:
					foundInList = True
			if not foundInList:
				found.append(Y)
		
		if set(found) == set(done):
			return ''.join(num)
	return "INSOMNIA"

results = []
firstLine = True
with open("A-large.in") as f:
	contents = f.readlines()
	for content in contents:
		if not firstLine:
			results.append(findIt(content.strip("\n")))
		firstLine = False;

file = open("a.out", "w")
counter = 1
for item in results:
	file.write("Case #" + str(counter) + ": " + item + "\n")
	counter += 1

file.close()