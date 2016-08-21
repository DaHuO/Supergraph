def lastNumber(n):
	digits = set()
	if n == 0:
		return "INSOMNIA"
	i = 0
	while(len(digits) != 10):
		i += 1
		[digits.add(c) for c in str(i * n)]
	return str(i * n)

with open("A-large.in",'r') as file:
	fileO = open("output.txt","w")
	T = int(file.readline())
	for j in range(T):
		fileO.write("Case #" + str(j + 1) + ": " + lastNumber(int(file.readline())) + "\n")
	fileO.closed
