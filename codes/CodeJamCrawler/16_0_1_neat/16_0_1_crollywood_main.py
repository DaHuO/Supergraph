
def main():
	solutions = []
	with open('A-large.in', 'r') as f:
		rows = int(f.readline())
		for i in range(rows):
			seen = [False]*10
			tc = int(f.readline())
			if tc == 0:
				solutions.append('INSOMNIA')
				continue
			counter = 1
			lastNumber = 0
			while(checkStatus(seen)):
				lastNumber = counter * tc
				seen = updateStatus(seen, lastNumber)
				counter += 1
			solutions.append(str(lastNumber))
	
	with open('A-large.out', 'w') as f:
		counter = 1
		for line in solutions:
			f.write("Case #{0}: {1}\n".format(str(counter), line))
			counter += 1


def updateStatus(seen, number):
	while number:
		digit = number % 10
		seen[digit] = True
		number //= 10
	return seen

def checkStatus(seen):
	return False in seen

main()
