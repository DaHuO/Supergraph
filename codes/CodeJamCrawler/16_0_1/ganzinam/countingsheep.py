import sys







def countingsheep(N):
	lastnumber = N.strip()
	history = []
	
	if int(lastnumber) == 0:
		return "INSOMNIA"
	else:
		multiplier = 0

		while len(history) != 10: #[0,1,2,3,4,5,6,7,8,9]
			multiplier += 1
			lastnumber = str(multiplier*int(N))

			for digit in lastnumber:
				if digit not in history:
					history.append(digit)
			
	return lastnumber




















if __name__ == "__main__":
	if len(sys.argv) > 1:
		filename = sys.argv[1]

	filename = "A-large.in"

	answer = ""
	with open(filename, "r") as f:
		maxcase = f.readline()
		case = 1
		while case < int(maxcase)+1:
			lastnumber = countingsheep(f.readline())
			answer += "Case #" + str(case) + ": " + lastnumber + "\n"
			case+=1

	print(answer)
	with open("A-large.out","w") as f:
		f.write(answer)
