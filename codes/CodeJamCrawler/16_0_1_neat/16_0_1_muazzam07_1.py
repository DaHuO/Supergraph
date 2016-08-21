# f = open("in1.txt")

# lines = f.readlines()
lines = [line.rstrip('\n') for line in open('A-large.in')]
# print lines

lines.remove(lines[0])
globecount = 1
print lines


myfile = open("out1.txt",'w')

for num in lines:
	counter = 1
	arr = ['0'] * 10
	tempnumstr = num
	tempnum = int(tempnumstr)
	tempnumold = 0
	while '0' in arr:
		if not num == '0':
			stringeachdigit = [i for i in tempnumstr]
			digitlist = map(int,stringeachdigit)#dividetodig(stringeachdigit)
			for eachdig in digitlist:
				if arr[eachdig] == '0':
					arr[eachdig] = '1'
			if counter >= 2000:
				tempnumold = "INSOMNIA"
				break
			
		else: 
			tempnumold = "INSOMNIA"
			break
		counter = counter + 1
		tempnumold = tempnum
		tempnum = int(num) * counter
		tempnumstr = str(tempnum)

	myfile.write("Case #" + str(globecount) + ": " + str(tempnumold) + "\n")
	globecount = globecount + 1

myfile.close()