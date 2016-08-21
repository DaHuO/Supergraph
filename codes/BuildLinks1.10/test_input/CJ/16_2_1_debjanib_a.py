from collections import defaultdict

T = int(raw_input())

for t in range(T):
	S = raw_input()
	numbers = [('Z', [0, "ZERO"]), 
	('W', [2, "TWO"]), 
	('U', [4,"FOUR"]), 
	('X', [6,"SIX"]), 
	('G', [8,"EIGHT"]), 
	('S', [7,"SEVEN"]),
	('F', [5,"FIVE"]),
	('R', [3, "THREE"]),
	('O', [1,"ONE"]),
	('E', [9, "NINE"])]

	m = defaultdict(int)
	for e in S:
		m[e] +=1
	l = [0 for i in range(10)]
	for n in numbers:
		num, arr = n
		if num in m and m[num]>0:
			l[arr[0]] +=m[num]
			temp = m[num]
			for letter in arr[1]:
				m[letter]-=temp
	res = ""
	for i in range(10):
		if l[i] > 0:
			res+= str(i)*l[i]

	print( "Case #%d: %s" % (t+1, res) )