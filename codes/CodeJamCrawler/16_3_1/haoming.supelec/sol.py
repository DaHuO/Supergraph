f = open("input")         
line = f.readline()

def isempty(dict):
	for i in dict:
		if dict[i] != 0:
			return False
	return True


def sum(dict):
	sum = 0
	for i in dict:
		sum += dict[i]
	return sum

def getdist(dict):
	count = 0
	for i in dict:
		if dict[i] != 0:
			count += 1
	return count

index = 1
while line:
	t = {}
	res = ""
	line = f.readline()
	line = f.readline().replace("\n", "")
	array = line.split(" ")
	if array[0] == "":
		break

	for i in range(len(array)):
		t[i] = int(array[i])

	#getmax
	while not isempty(t):

		match = False
		if getdist(t) == 3 and sum(t) == 3:
			for i in t:
				if t[i] == 1:
					t[i] = 0
					res += chr(i+65) + " "
					match = True
					break
		elif getdist(t) == 2 and sum(t) == 2:
			for i in t:
				if t[i] == 1:
					t[i] = 0
					res += chr(i+65)
					match = True
		elif getdist(t) == 2 and sum(t) == 3:
			for i in t:
				if t[i] == 2:
					t[i] = 1
					res += chr(i+65) + " "
					match = True
					break
		if match:
			continue






		max = 0
		maxindex = -1
		for i in t:
			if max < t[i]:
				max = t[i]
				maxindex = i

		#get if max is double
		max2flag = False
		max2index = -1
		for i in t:
			if max == t[i] and maxindex != i:
				max2index = i
				max2flag = True
				break

		if max2flag:
			t[maxindex] -= 1
			t[max2index] -= 1
			res += chr(maxindex+65) + chr(max2index+65) + " "

		elif t[maxindex] == 1:
			t[maxindex] -= 1
			res += chr(maxindex+65) + " "

		else:
			t[maxindex] -= 2
			res += chr(maxindex+65) *2 + " "

	print "Case #" + str(index) + ": " + res
	index += 1

f.close()