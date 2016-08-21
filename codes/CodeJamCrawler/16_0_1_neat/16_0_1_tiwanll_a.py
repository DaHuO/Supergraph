allnums = [int(x) for x in "1234567890"]

def f(n):
	global allnums
	full = allnums[:]

	for i in range(10000):
		m = (i+1)*n
		#print(m)
		num = [int(x) for x in str(m)]
		full = [x for x in full if x not in num]
		#print(full)
		if len(full)==0:
			return m
	return "INSOMNIA"


inputfile = open("A-large.in", "r")
outputfile = open("A.out", "w")
t = int(inputfile.readline().strip())
for case in range(t):
	n = int(inputfile.readline().strip())
	#print("CASE")
	#print(n)
	ans = f(n)
	outputfile.write("Case #%s: %s\n" % (case+1, str(ans)))
	#print(ans)

