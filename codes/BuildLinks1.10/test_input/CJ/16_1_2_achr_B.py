from itertools import combinations

def transpose(matrix):
	return [list(x) for x in zip(*matrix)]

def f(N, rows):
	for combination in combinations(enumerate(rows), N):
		indices = [index for index, row in combination]
		matrix = [row for index, row in combination]
		matrix = transpose(matrix)

		filteredRows = [row for index, row in enumerate(rows) if index not in indices]
		# print("Matrix", matrix)
		# print("Filtered", filteredRows)

		if all(filteredRow in matrix for filteredRow in filteredRows):
			for row in matrix:
				if row not in filteredRows:
					return row

T = int(input())
for t in range(1, T+1):
	N = int(input())
	rows = []

	for n in range(2*N-1):
		row = list(map(int, input().split()))
		rows.append(row)

	rows.sort()
	print("Case #{}: {}".format(t, ' '.join(map(str, f(N, rows)))))