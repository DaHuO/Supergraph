def countingsheep(x):
	#special case if 0
	if x=='0':
		return "INSOMNIA"
	else:
		N = int(x)
		checker = [0,0,0,0,0,0,0,0,0,0]
		multiplier = 1 #increment for every count
		while (sum(checker) != 10):
			multiplier += 1
			#iterate through digits to check if not already seen
			for digit in x:
				if checker[int(digit)] == 0:
					checker[int(digit)] = 1
				#check if can return
				if (sum(checker) == 10):
					return x
			x = str(N*multiplier)

def countingSheepHelper(filename):
	f = open(filename, 'r')
	f2 = open('output.txt', 'w')
	case = 0
	T = 0
	for line in f.readlines():
		if case == 0:
			T = int(line.rstrip())
		else:
			N = line.rstrip()
			out = ["CASE #",str(case),": ",countingsheep(N)]
			result = "".join(out)
			f2.write(result+'\n')
		case += 1



countingSheepHelper('A-large.in.txt')