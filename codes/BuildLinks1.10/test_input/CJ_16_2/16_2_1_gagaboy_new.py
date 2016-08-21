t = int(raw_input())

for i in range(1,t+1):
	#print i
	ans = "Case #"+str(i)+": "
	s = raw_input()
	s = s.lower()
	numbers = []
	templ = list(s)


	if 'z' in templ:
		zero = "zero"
		f = templ.count('z')
		for i in range(0,f):
			numbers.append(0)
			for ch in zero:
				templ.remove(ch)


	if 'w' in templ:
		two = "two"
		f = templ.count('w')
		for i in range(0,f):
			numbers.append(2)
			for ch in two:
				templ.remove(ch)



	if 'x' in templ:
		six = "six"
		f = templ.count('x')
		for i in range(0, f):
			numbers.append(6)
			for ch in six:
				templ.remove(ch)


	if 'g' in templ:
		eight = "eight"
		f = templ.count('g')
		for i in range(0, f):
			numbers.append(8)
			for ch in eight:
				templ.remove(ch)


	if 't' in templ:
		three = "three"
		f = templ.count('t')
		for i in range(0, f):
			numbers.append(3)
			for ch in three:
				templ.remove(ch)
	
	if 's' in templ:
		seven = 'seven'
		f = templ.count('s')
		for i in range(0,f):
			numbers.append(7)	
			for ch in seven:
				templ.remove(ch)
	#print numbers
	#print templ



	if 'v' in templ:
		five = "five"
		f = templ.count('v')
		for i in range(0, f):
			numbers.append(5)
			for ch in five:
				templ.remove(ch)
	#print numbers
	#print templ

	if 'f' in templ:
		four = "four"
		f = templ.count('f')
		for i in range(0, f):
			numbers.append(4)
			for ch in four:
				templ.remove(ch)

	if 'o' in templ:
		one = "one"
		f = templ.count('o')
		for i in range(0, f):
			numbers.append(1)
			for ch in one:
				templ.remove(ch)
	#print numbers
	#print templ

	if 'n' in templ:
		nine = "nine"
		f = templ.count('n')
		f/=2
		for i in range(0, f):
			numbers.append(9)
			for ch in nine:
				templ.remove(ch)

	numbers.sort()
	for num in numbers:
		ans+=str(num)
	print ans















		


