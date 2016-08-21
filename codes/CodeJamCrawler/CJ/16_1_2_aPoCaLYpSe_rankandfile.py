import copy
import sys
import math
import numpy as np

sys.setrecursionlimit(10000)

def parse_case(instrm):
	n = int(instrm.readline().strip())
	rows = []
	for i in range(2*n - 1):
		rows.append([int(i) for i in instrm.readline().strip().split()])
	return rows
	

def bvec(n, ntrue):
	if n == 1:
		yield [ntrue == 1]
		return
	
	if n == ntrue:
		yield [True]*n
		return
	
	for rec in bvec(n-1, ntrue):
		yield [False] + rec
	
	if ntrue > 0:
		for rec in bvec(n-1, ntrue-1):
			yield [True] + rec

		
def solve_case(case):
	rows = case
	rows.sort()
	nrows = len(rows)
	n = len(rows[0])
	mat = np.array(rows)
	twopown = int(2**nrows)
	
	res = None
	for barr in bvec(nrows, n):
		barr = np.array(barr)
		assert len(barr) == nrows
		assert sum(barr) == n, "sum barr: {}".format(sum(barr))
		mat1 = mat[barr]
		mat2 = mat[~barr]
		mat1t = mat1.transpose()
		for j in range(n):
			mat2plus = np.row_stack((mat2[:j], mat1t[j], mat2[j:]))
			if (mat2plus == mat1t).all():
				res = mat1t[j]
		if res is not None:
			break
				
	assert res is not None
	return " ".join(str(i) for i in res)


if __name__ == "__main__":
	instrm = open(sys.argv[1])
	ncases = int(instrm.readline().strip())
	for i in range(ncases):
		case = parse_case(instrm)
		ans = solve_case(case[::-1])
		print("Case #{}: {}".format(i+1, ans))
