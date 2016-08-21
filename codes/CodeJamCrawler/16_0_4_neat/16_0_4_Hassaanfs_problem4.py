def giveIndexArray(k, c, s):
	if(k == 1):
		return [1]
	else:
		lst = []
		fracLen = k**c
		step = (fracLen - 1)/(k - 1)
		num = 1
		while(num <= fracLen):
			lst.append(num)
			num += step
		return lst

if __name__ == "__main__":
	lines = [line.rstrip('\n') for line in open('D-small-attempt1.in')]
	count = 0
	f = open('output.txt', 'w')
	for string in lines:
		if(count != 0):
			arr = string.split(' ')
			k = int(arr[0])
			c = int(arr[1])
			s = int(arr[2])
			indices = giveIndexArray(k, c, s)
			f.write("Case #"+str(count)+": " + ' '.join([str(x) for x in indices]) + "\n")
		count += 1
	f.close()