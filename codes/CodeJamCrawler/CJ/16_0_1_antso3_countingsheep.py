f = file("input.in", "r");
lines = f.readlines()
lines = map(lambda x: x[:-1], lines)

def getres(n):
	init = n
	nums = []
	for i in range(0, 10):
		nums.append(str(i))
	if n == 0:
		return "INSOMNIA"
	while True:
		digits = list(str(n))

		for j in digits:
			if j in nums:
				nums.remove(j)
		
		if len(nums) == 0:
			return str(n)
		
		n += init
		
	

T = int(lines[0])
f.close()
g = file("output.out", "w")
for i in range(1, T+1):
	g.write("Case #" + str(i) + ": " + getres(int(lines[i])) +"\n")

g.close()
