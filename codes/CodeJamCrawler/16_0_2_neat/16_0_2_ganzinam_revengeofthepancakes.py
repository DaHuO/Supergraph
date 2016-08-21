import sys







def revenge(N):
	flipcount = 0

	if len(N) != 1:
		dish = N
		optimal_dish = "+"*len(N)
		ng_optimal_dish = "-"*len(N)

		#print(dish, optimal_dish, dish == optimal_dish)

		while dish != optimal_dish:
			i = 0
			ps = dish[0]
			flipped = False

			while i < len(dish) and flipped == False:
				if dish[i] != ps:
					dish = flip(dish,i)
					flipcount+=1
					flipped = True
				elif dish == ng_optimal_dish:
					dish = flip(dish, len(dish))
					flipcount+=1
					flipped = True
				else:
					i+=1
	else:
		if N[0] != "+":
			flipcount = 1

	return flipcount


def flip(dish, i):
	"""
	flip the pancakes from top upto position i
	"""
	if dish[0] == "-":
		dish = "+"*i + dish[i:]
	else:
		dish = "-"*i + dish[i:]
	return dish



if __name__ == "__main__":
	if len(sys.argv) > 1:
		filename = sys.argv[1]

	filename = "B-large.in"


	answer = ""
	with open(filename, "r") as f:
		maxcase = f.readline()
		case = 1
		while case < int(maxcase)+1:
			numberofflips = revenge(f.readline().strip())
			answer += "Case #" + str(case) + ": " + str(numberofflips) + "\n"
			case+=1
	
	with open("B-large.out","w") as f:
		f.write(answer)