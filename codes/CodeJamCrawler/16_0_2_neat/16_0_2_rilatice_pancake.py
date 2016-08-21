def pancake(input):
	count = 0
	last = '+'
	for curchar in input[:: -1] :
		if(curchar != last):
			count += 1
			last = curchar
	return count



inf = open("B-large.in","r")
outf = open("result.txt","w")
length = int(inf.readline())
for i in range(length):
	input = inf.readline().strip('\n')
	result = pancake(input)
	outf.write('Case #%s: %s' %(i+1,result))
	if i < length -1:
		outf.write('\n')
inf.close()
outf.close()