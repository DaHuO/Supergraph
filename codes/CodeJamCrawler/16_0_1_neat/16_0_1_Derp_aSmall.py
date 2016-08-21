BIG_NUM = 999999999

def allKeysIn(s):	
	for i in range(10):		
		if i not in s:			
			return False
	return True
	
def calculateStep(n):
	store = set()
	n = int(n)
	cont = False
	mult = 1
	old = None
	while (not cont) :
		curr = str(n*mult)
		for a in curr:
			store.add(int(a))
		cont = allKeysIn(store)
		
		mult = mult+1
		if mult>=BIG_NUM or (old is not None and old==curr):
			return "INSOMNIA"
			break
		old = curr
	return curr

def main():
	testCount = raw_input()
	initNums=list()
	for i in range (0,int(testCount)):
		initNum = raw_input()
		initNums.append(initNum)

	for i in range(0,len(initNums)):
		num = initNums[i]
		result = calculateStep(num)	
		print "Case #"+str(i+1) + ": " + str(result)
		

if __name__ == '__main__':
	main()