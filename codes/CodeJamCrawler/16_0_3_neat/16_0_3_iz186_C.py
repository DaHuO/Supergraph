def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n/base,base) + convertString[n%base]

def check(newNum):
	if newNum == 2:
		return -1
	if newNum == 3:
		return -1
	if newNum == 5:
		return -1
	if newNum % 2 == 0:
		return 2
	if newNum % 3 == 0:
		return 3
	if newNum % 5 == 0:
		return 5
	i = 7
	while i * i <= newNum:
		if newNum % i == 0:
			return i
		i += 2
	return -1

with open('C.in', 'r') as fin:
	with open('c.out', 'w') as fout:
		T = int(fin.readline())
		for case in range(1, T+1):
			fout.write("Case #" + str(case) + ":\n")
			NJ = fin.readline()
			N = int(NJ.split()[0])
			J = int(NJ.split()[1])
			s = "1"
			for i in range(1, N):
				s += "0"
			start = int(s,2)
			start += 1
			while J != 0:
				num = toStr(start,2)
				if num[0] == "1" and num[-1] == "1":
					condition = True
					arr = []
					for base in range(2, 11):
						newNum = int(num, base)
						arr.append(check(newNum))
						if arr[-1] == -1:
							condition = False
							break
					if condition:
						fout.write(num)
						for thing in arr:
							fout.write(" " + str(thing))
						fout.write("\n")
						J -= 1
						print(J)
				start += 1