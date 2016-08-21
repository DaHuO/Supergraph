def inputvars():
	f = open('QualifierInput.txt')
	num = int(f.readline())
	numlist = f.read().splitlines()
	return num, numlist

def outputvars(num, output):
	f = open('output.txt', 'w')
	for x in range(num):
		f.write(str('Case #' + str(x + 1) + ': ' + output[x] + '\n'))
	f.close()

def main():
	maxiterations = 100000000
	num, numlist = inputvars()
	output = []
	for x in range(num):
		curnum = numlist[x]
		iterations = 0
		iterationsbchange = 0
		vals = set()
		numvals = 0
		y = 1
		while(iterationsbchange < maxiterations):
			if(numvals >= 10):
				output.append(curnum)
				break
			curnum = str(y * int(numlist[x]))
			iterations += 1
			vals = vals.union(set(list(curnum)))
			if(len(vals) == numvals):
				iterationsbchange += 1
			else:
				iterationsbchange = 0
				numvals = len(vals)
			temp = int(curnum)
			y += 1
		if(iterationsbchange == maxiterations):
			output.append('INSOMNIA')
	outputvars(num, output)

main()