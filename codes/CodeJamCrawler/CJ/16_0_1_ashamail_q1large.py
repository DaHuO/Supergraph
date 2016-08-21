def checknumber(n):
	checkarray = [False, False, False, False, False, False, False, False, False, False]
	digits = [0,1,2,3,4,5,6,7,8,9]
	i = 1;
	while True:
		num = i*n
		splitnumber = map(int,str(num))
		for x in splitnumber:
			if x in digits:
				checkarray[x] = True
				last = x
		if (all(checkarray)):
			return num
		i += 1



def main():
	f = open('A-large.in', 'r')
	fout = open('outfilelarge.in', 'w')
	num = 0
	iterator = 1
	line = (f.readline()).rstrip()
	while(line != ''):
		print "next iteration"
		print ("line + ", line)
		num = line
		print num
		if (int(num) < 1 or int(num) > 100):
			print "Value of T not in range"
			break
		for i in range(0,int(num)):
			value = (f.readline()).rstrip()
			if(int(value) < 0 or int(value) > 1000000):
				break
			if(int(value) == 0):
				output = "INSOMNIA"
			else:
				output = checknumber(int(value))

			add = "Case #" + str(iterator)  + ": "
			final = add + str(output)
			fout.write(final+'\n')
			iterator += 1
			
		line = (f.readline()).rstrip()

	f.close()
	fout.close()

if __name__ == '__main__':
	main()