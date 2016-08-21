TEST_NAME = 'B-large'

def main():
	solutions = []
	with open(TEST_NAME+'.in', 'r') as f:
		rows = int(f.readline())
		for i in range(rows):
			all_heights = [0 for i in range(2501)]
			N = int(f.readline().strip())
			
			for j in range(2*N-1):
				row = (map(int, f.readline().strip().split(' ')))
				for number in row:
					all_heights[number] += 1

			solution = get_odd_heights(all_heights)
			
			solutions.append(' '.join((map(str, solution))))
	
	with open(TEST_NAME+'.out', 'w') as f:
		counter = 1
		for line in solutions:
			f.write("Case #{0}: {1}\n".format(str(counter), line))
			counter += 1

def get_odd_heights(all_heights):
	res = []
	counter = 0
	for i in all_heights:
		if i % 2 != 0:
			res = insert_sorted(counter, res)
		counter += 1
	return res
	
def insert_sorted(x, niz):
	res = []
	counter = 0
	for i in niz:
		if i < x:
			counter += 1
		else:
			break
	res = niz[:counter] + [x] + niz[counter:]
	return res

main()

