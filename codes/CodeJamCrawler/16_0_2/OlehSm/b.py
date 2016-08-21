a = open("b_l.in", 'r')
answer = open("answer_b_big.txt", 'w')

n = int(a.readline().strip())

for i in range(n):
	cake = a.readline().strip()
	bool = True
	count = 0
	last = cake[-1]
	for l in cake[::-1]:
		if last!= l:
			if not bool and last == "+":
				count += 1
				bool = not bool
			if bool and last == "-":
				count += 1
				bool = not bool
		last = l
		
	if not bool and last == "+":
		count += 1
	if bool and last == "-":
		count += 1
	
	print(count)
	
	answer.write("Case #" + str(i+1) + ": " + str(count) + "\n")