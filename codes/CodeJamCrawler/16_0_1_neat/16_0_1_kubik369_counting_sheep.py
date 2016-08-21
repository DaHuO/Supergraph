'''from random import randint

for l in range(100):
	i = randint(0, 10**6)
	#print(i)
	s = set()	
	#print("number: " + str(i))
	for j in range(1,100):
		x = i * j
		while x > 0:
			s.add(x % 10)
			x //= 10
	#print(s)
	if len(s) != 10:
		print(i)
'''

for i in range(int(input())):
	n = int(input())
	s = set()
	ans = -1
	for j in range(1,1000):
		x = n * j
		while x > 0:
			s.add(x % 10)
			x //= 10
		if len(s) == 10:
			#print("x is" + str(n * j))
			ans = n * j
			break
	#print(s)
	if ans == -1:
		print("Case #" + str(i + 1) + ": INSOMNIA")
	else:
		print("Case #" + str(i + 1) + ": " + str(ans))