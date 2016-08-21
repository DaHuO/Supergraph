import numpy as np
import fileinput

l = []

for i in fileinput.input():
	if i:
		l.append(int(i.replace("\n","")))

# print l

#remove # test cases
l = l[1:]

caseNum = 1
for n in l:
	# n = l[0]
	# n = '0'
	insomnia = 0
	fall_asleep = 0
	# print n
	digits_seen = []
	all_new_nums = []
	index = 1
	while (not fall_asleep):
		newNum = int(n) * index
		# print newNum
		for digit in str(newNum):
			#havent seen num
			if not digit in digits_seen:
				digits_seen.append(digit)
		if (not newNum in all_new_nums):
			all_new_nums.append(newNum)		
		else:
			print "Case #%s: INSOMNIA" %caseNum
			caseNum+=1	
			insomnia = 1
			break	
		if len(digits_seen) == 10:
			fall_asleep = 1

		index += 1
	# print digits_seen
	# print all_new_nums[-1]
	if not insomnia:
		print "Case #%s: %s" %(caseNum, all_new_nums[-1])
		caseNum+=1	

