# fname = "first.txt"
fname = "A-large.in"
ofname = "largeout.txt"

nums = ["0","1","2","3","4","5","6","7","8","9"]
def main():
	caseCount = 1
	with open(fname, 'r') as f:
		first_line = f.readline().rstrip('\n')
		# print(first_line)
		for d in range(int(first_line)):
			r = f.readline().rstrip('\n')
			# print (r)
			t = str("Case #"+str(caseCount)+": "+str(getNums(int(r))))
			print(t)
			addToOutF(t)
			caseCount = caseCount + 1
			reset()


def reset():
	global nums
	nums = ["0","1","2","3","4","5","6","7","8","9"]

def getNums(z):
	# print(z)
	nCount = 2
	if z == 0:
		return "INSOMNIA"
	else:
		t = z
		removeOld(splitNumber(z))
		while not checkCorrect():
			t = nCount*z
			nCount = nCount+1
			removeOld(splitNumber(t))
	return t


def removeOld(numbrs):
	for x in numbrs:
		if x in nums:
			nums.remove(x)

def splitNumber(num):
	return [a for a in str(num)]

def checkCorrect():
	if nums == []:
		return True
	else:
		return False

def addToOutF(txtbby):
	outfile = open(ofname, 'a')
	outfile.write(txtbby)
	outfile.write("\n")

main()