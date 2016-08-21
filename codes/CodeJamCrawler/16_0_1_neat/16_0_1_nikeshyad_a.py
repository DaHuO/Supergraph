myfile = open('file.txt','r')
data = []
for line in myfile:
	line = line.rstrip()
	data.append(line)

data = data[1:]

def notContainsDigit(val):
	digits = ['0','1','2','3','4','5','6','7','8','9']
	return sorted(val) != digits


result = []
for x in data:
	if int(x) == 0:
		result.append("Insomnia")
		continue
	val = []
	n = 1
	while notContainsDigit(val):
		num = int(x)*n
		for i in str(num):
			#print i
			if i not in val:
				val.append(i)
		n+=1
	result.append(int(x)*(n-1))
		#print val

for i in range(len(data)):
	print "Case #" + str(i+1) + ": " + str(result[i])