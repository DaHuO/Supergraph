# Uses https://github.com/DarioFanucchi/CompetitionCode.git
import sys
sys.path.insert(0, "../../../CompetitionCode")
import codejam_io

def digits(N):
	return [int(d) for d in str(N)]

def solve_case(c):
	found = [0 for i in xrange(10)]
	nfound = 0
	N = c[0]

	for k in xrange(1,2000000):
		for d in digits(k*N):
			if(not found[d]):
				nfound += 1
				found[d] = True
		if nfound >= 10:
			return k*N
	return "INSOMNIA"

def solve(fin, fout):
	L = codejam_io.read_simple(fin, int)
	S = map(solve_case, L)
	codejam_io.write_simple(fout, S)

#solve("A-sample.in", "A-sample.out")
#solve("A-small-attempt0.in", "A-small-attempt0.out")
solve("A-large.in", "A-large.out")