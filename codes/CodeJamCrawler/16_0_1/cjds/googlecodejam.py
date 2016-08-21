filename='output'
target = open(filename, 'w')

def printer(data):
	target.write("Case #%d: %s"%(data[0],data[1]))
	target.write("\n")

digits=[False]*10
with open("A-large.in", "r") as ins:
	T=int(ins.readline())

	for i in range(1,T+1):
		digits=[False]*10
		N=int(ins.readline())
		if N==0:
			printer([i,"INSOMNIA"])
		else:
			c=0
			while not all(digits):
				c+=1
				split=[int(a) for a in str(N*c)]	
				for digit in split:
					digits[digit]=True
			printer([i,str(N*c)])


