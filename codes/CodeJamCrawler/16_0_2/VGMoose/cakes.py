trials = int(raw_input())
for t in range(0, trials):
	strin = raw_input()
	lastchar = "+"
	total = 0

	strin = strin[::-1]

	for char in strin:
		if char != lastchar:
			total += 1
			lastchar = char

	print("Case #" + str(t+1) + ": " + str(total))
	
