import sys

def main():
	name, pathin, pathout = sys.argv

	filein = open(pathin)
	fileout = open(pathout,'w')

	total = int(filein.readline())
	results = []
	for case in range(total):
		N = int(filein.readline())
		lis = []
		for i in range(2*N-1):
			lis.append(filein.readline().split())

		results.append(solve(lis))

	for i, result in enumerate(results):
		fileout.write('Case #%s: %s\n'%(i+1, result))

def solve(lis):

	di = {}
	for li in lis:
		for el in li:
			di[el] = di.get(el, 0) + 1

	results = []
	for el in di:
		if di[el] % 2 == 1:
			results.append(int(el))

	results = sorted(results)

	return ' '.join([str(_) for _ in results])




if __name__ == '__main__':
	main()

