with open("A-large.in", "r") as f:
	t = int(f.readline())


	result = ""
	parties = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	for i in range(t):
		n = int(f.readline())
		senators = [int(j) for j in f.readline().split()]
		result += "Case #" + str(i+1) + ":"
		while sum(senators) > 0:
			result += " "
			index = senators.index(max(senators))
			senators[index] -= 1
			result += parties[index]
			
			if sum(senators) > 0:
				index = senators.index(max(senators))
				senators[index] -= 1
			
				if max(senators) <= sum(senators)//2:
					result += parties[index]
				else:
					senators[index] += 1
		
		
		result += '\n'
		
	
with open("output.txt", "w") as f:
	f.write(result)
