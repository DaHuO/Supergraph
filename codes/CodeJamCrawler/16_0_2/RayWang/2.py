#encoding=utf8
filename = "B-large.in"
raw_data = ''
with open(filename, 'r') as f:
	raw_data = f.read().split('\n')

def valueSet(value):
	for count in range(len(value)):
		cura[count] = 1 if value[count] == '+' else 0

test_count = int(raw_data.pop(0))
for test in range(test_count):
	curStr = raw_data.pop(0)
	#print curStr
	#cura = [0] * len(curStr)
	#valueSet(curStr)

	tempchar = curStr[0]
	count2 = 0 if curStr[len(curStr)-1] == '+' else 1
	
	for temp in range(len(curStr)):
		if curStr[temp] != tempchar:
			count2 += 1
			tempchar = curStr[temp]

	print 'Case #%d: '%(test+1),count2
