allDigits = set(str(i) for i in range(10))

def sheepSleep(N):
	
	if N == 0:
		return "INSOMNIA"

	test = set()
	for i in range(1, 100):
		number = i*N
		test = test.union(set(str(number)))

		if(test == allDigits):
			return number

test = open("A-large.in", 'r')
a = open("counting_sheep_large.txt", 'w')
b=1

for i in list(test)[1:]:
	a.write("Case #%d: %s\n" % (b, str(sheepSleep(int(i)))));
	b=b+1

a.close()