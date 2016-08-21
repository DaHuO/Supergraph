import math

a = open("new.txt", 'r')
answer = open("answer_c.txt", 'w')

n = int(a.readline().strip())

prime = {}

for i in range(n):
	answer.write("Case #" + str(i+1) + ":\n")
	a, b = (int(l) for l in a.readline().strip().split())
	num = "1" + "0"*(a-2) + "1"
	q = bin(int(num, 2))
	count = 0
	while q != bin(int('1' + '0'*a, 2)):	
		if str(q)[-1] == '0':
			q = bin(int(q, 2) + 1)
			continue
		
		qwer = []
		asd = True
		print(q, count)
		for z in range(2, 11):
			w = int(q[2:], z)
			for c in range(2, math.ceil(math.sqrt(w))):
				if w//c == w/c:
					qwer.append(c)
					asd = False
					break
			if asd:
				break
		if len(qwer) == 9:
			answer.write(q[2:] + " ")
			for i in range(9):
				answer.write(str(qwer[i]) + " ")
			answer.write("\n")
			count += 1 
		
		if count == b:
			break
		
		q = bin(int(q, 2) + 1)
	
	