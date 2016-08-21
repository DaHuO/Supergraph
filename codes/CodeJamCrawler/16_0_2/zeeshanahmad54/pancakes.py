#pancakes.py
import re
pattern1 = re.compile(r"\b\++\-+\b")
pattern2 = re.compile(r"\b\-+\++\b")
plus = re.compile(r'\+')
minus = re.compile(r'\-')


cases = int(raw_input())


for i in range(cases):
	counter = 0
	str1 = raw_input()
	if(all(item == '+' for item in str1)):
		answer = 0
	elif(all(item == '-' for item in str1)):
		answer = 1
	elif(pattern1.match(str1)):
		answer = 2
	elif(pattern2.match(str1)):
		answer = 1
	else:
		while(1):
			# a = list(str1)
			# print(a)
			l = re.findall(r'((.)\2*)', str1)
			lst = [x[0] for x in l]
			# print lst
			# print len(lst)

			if (re.match(r'\++',lst[0])):
				# plus.sub(r'\-',lst[0])
				lst[0] = re.sub(r'\+', r'-', lst[0])
				counter = counter +1
			elif(re.match(r'\-+',lst[0])):
				# minus.sub(r'\+'.lst[0]))
				lst[0] = re.sub(r'-', r'+', lst[0])
				counter = counter +1
			# print(lst)
			str1 = ''.join(lst)
			# print str1
			if(all(item == '+' for item in str1)):
				break
		answer = counter




	print "case #"+str(i+1)+": "+str(answer) 
