#encoding=utf8
filename = "A-large.in"

def valueTest(value):
	while value != 0 :
		flag[value%10] = 1
		value /= 10

raw_data = ''
with open(filename, 'r') as f:
	raw_data = f.read().split('\n')



test_count = int(raw_data.pop(0))
for test in range(test_count):
	cur = int(raw_data.pop(0))
	flag = [0,0,0,0,0,0,0,0,0,0]
	#       0 1 2 3 4 5 6 7 8 9

	if cur == 0 :
		print 'Case #%d:'%(test+1), 'INSOMNIA'
	else :
		count2 = 0
		while count2 < 100:
			valueTest(cur*count2)
			for count in range(0,10):
				if flag[count] == 0:
					break
			if count == 9 and flag[9] == 1:
				break;
			count2+=1
		print 'Case #%d:'%(test+1), (cur * count2)
		

