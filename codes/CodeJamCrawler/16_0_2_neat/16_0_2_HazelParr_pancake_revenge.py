T = int(input())

for case in range(T): 
	x = input()
	count = 0
	while "-" in x:
		new_string = ""
		unchanged = ""
		y = x.rfind("-")
		fragment = x[:y+1]
		unchanged = x[y+1:]
		for i in fragment:
			if i == "-":
				new_string += "+"
			else:
				new_string += "-"
		count += 1
		x = new_string + unchanged
		
	print("Case #{}: {}".format(case+1, count))

