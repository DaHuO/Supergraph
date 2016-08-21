import math

lines = [line.rstrip('\n') for line in open('C-small-attempt0.in')]

lines.remove(lines[0])
globecount = 1
# print lines
lines = lines[0].split()
# print lines
myfile = open("out3.txt",'w')

count = 0

def funcisprime(num):
	# numori = num
	for i in range(2,int(math.sqrt(num/2))):
		if num%i == 0:
			return i
	return -1

def based(s,base):
	i = len(s) - 1
	j = 0
	num = 0
	while not i < 0:
		num = num + s[i] * base ** j
		i = i - 1
		j = j + 1
	return num

myfile.write("Case #" + str(globecount) + ':'+'\n')
i = 0
s = [1]
while i < (int(lines[0])-2):
	s.append(0)
	i = i+1
s.append(1)

# print s

for x in range(0,(2**(int(lines[0])-2))):
	inter = 1
	arr = []
	temp = x
	for intrmdt in range(0,(int(lines[0])-2)):
		if temp % 2 == 1:
			s[int(lines[0])-2-intrmdt]= 1
		else:
			s[int(lines[0])-2-intrmdt] = 0
		temp = temp / 2
	if count < int(lines[1]):
		findnext = 0
		for base in range(2,11):
			arr.append(funcisprime(based(s,base)))
			if arr[-1] == -1:
				inter = 0
				break
		if inter == 1:
			count = count + 1
			# print arr
			myfile.write(''.join([str(x) for x in s]) + ' ' + ' '.join(str(y) for y in arr) + '\n')
		
	else:
		# print lines[1]
		# print "here"
		break

	del arr[:]
	# count = count + 1

myfile.close()