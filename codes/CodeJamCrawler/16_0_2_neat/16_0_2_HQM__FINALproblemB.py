def Straighten(line):
	flag = 0
	it = 0 # will tell how deep into the string we are
	count = 0
	line_new = str(line)
	for s in line:
		if (flag == 0): # first iteration
			flag = 1
			prev = line_new[0]
			if(len(line)==1): # first and last
				if(s=='-'):
					count+=1
		else: # remaining iterations
			if(it==len(line)-1): # the very last index
				if (prev == '+'):
					if (s == '+'):
						break
					else:
						count +=2
				else: # prev is - and last index
					if(s == '+'):
						count+=1
					else:
						count+=1
			else: # not the last iteration
				if not(s == prev):
					count +=1
					prev = s
		it += 1
	print 'Final line: '+line
	return count


def Setter():
	inFile = open("problemBinp.txt", 'r')
	outFile = open('problemBout.txt','w')
	flag = 0
	i = 0 
	for line in inFile:
		line = line.rstrip()
		if (flag == 0):
			flag = 1
			numInp = int(line)
		else:
			if(numInp < i):
				break;
			else:
				print 'INPUT # '+str(i)
				ans = Straighten(line)
				outStr = 'Case #' + str(i) + ': '+ str(ans)+'\n'
				outFile.write(outStr)
		i += 1
	outFile.close()
	newOut = open('problemBout_edit.txt', 'w')
	with open('problemBout.txt', 'r') as newIn:
		data = newIn.read()
	newOut.write(data.rstrip())


def main():
	Setter()

if __name__ == '__main__':
	main()