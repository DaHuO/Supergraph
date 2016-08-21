#encoding=utf8
filename = "C-small-attempt0.in"

raw_data = ''
with open(filename, 'r') as f:
	raw_data = f.read().split('\n')

def createPrimeTable(tableSize):
	powValue = tableSize
	tempTable = [0] * powValue
	table = [] 
	for count in range(2,powValue):
		curValue = 2
		if tempTable[count] != 0 :
			continue

		while count * curValue < powValue:
			tempTable[count * curValue] = 1
			curValue +=1

	count2 = 0
	for count in range(2,powValue):
		if tempTable[count] == 0:
			table.insert(len(table), count)
	return table

def to2Base(value):
	r = []
	while value != 0:
		r.insert(0, 1 if value % 2 == 1 else 0)
		value /=2
	return r

def aryToValue(ary, base):
	r = 0
	for count in range(0, len(ary)):
		r = r + ary[count] * (base ** count)
	return r

test_count = int(raw_data.pop(0))
temp = raw_data.pop(0)
ques = temp.split(' ')
test = 2**( int(ques[0]) - 1) + 1
end = int(ques[1])
table = createPrimeTable( 65533 )
sucCount = 0
#print ques[0]
#print to2Base(test) 
#print aryToValue(to2Base(test),3) 
#print table
ans = [0]*11
print 'Case #1:'
while sucCount < end and test < 2**( int(ques[0]) ):
	test = 63

	curAry = to2Base(test)[::-1]
	for count in range(2, 11): #2 to 10 base
		value = aryToValue(curAry, count)
		#print test, count, value
		passvalue = 0
		aryCount = 0
		for aryCount in range(0, len(table)):
			if value % table[aryCount] == 0 and value != table[aryCount]:
				ans[count] = table[aryCount]
				passvalue = 1
				break
		
		if aryCount == len(table) - 1 and passvalue == 0:
			break

	if count == 10 and passvalue == 1:
		sucCount += 1
		ary2 = curAry[::-1]
		print ''.join(str(e) for e in ary2),ans[2],ans[3],ans[4],ans[5],ans[6],ans[7],ans[8],ans[9],ans[10]
	
	test += 2
	#cura[count] = 1 if value[count] == '+' else 0