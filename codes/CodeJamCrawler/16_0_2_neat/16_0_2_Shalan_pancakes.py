def read_file(name):
	with open(name) as file:
		for line in file:
			yield line

def remove_trailing_pluses(arr):
	while len(arr) > 0 and arr[-1]:
			arr.pop()
			
def solve(lines):
	numCases = int(next(lines))
	for i in range(1,numCases+1):
		arr = [True if x == '+' else False for x in next(lines).strip('\n')]
		remove_trailing_pluses(arr)
		count = 0
		n = len(arr)
		while True:
			remove_trailing_pluses(arr)
			if len(arr) == 0:
				break
			j = 0
			if arr[j]:
				count += 1
				while arr[j]:
					arr[j] = False
					j += 1
			arr = list(reversed([not x for x in arr]))
			count += 1
		
		print('Case #' + str(i) + ': ' + str(count))

if __name__ == '__main__':
	solve(read_file('input/pancakes.in'))
			
		