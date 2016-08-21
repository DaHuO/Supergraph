# Uses https://github.com/DarioFanucchi/CompetitionCode.git
import sys
sys.path.insert(0, "../../../CompetitionCode")
import codejam_io

def reduceAll(c, L1, L2):
	pos = [i for i, j in enumerate(c) if j == L1]
	if len(pos)%2 == 0:
		pattern = [''.join([chr(65+pos[k]), chr(65+pos[k+1])]) for k in xrange(0, len(pos), 2)]
	else:
		pattern = [chr(65+pos[0])] + [''.join([chr(65+pos[k]), chr(65+pos[k+1])]) for k in xrange(1, len(pos), 2)]
	for i in pos:
		c[i] = L2
	return pattern * (L1-L2)

def reduceCase(c):
	L1 = 0
	L2 = 0
	for i,elt in enumerate(c):
		if elt > L1:
			L2 = L1
			L1 = elt
		elif elt > L2 and elt < L1:
			L2 = elt 

	return reduceAll(c, L1, L2)


def solve_case(c):
	solution = []
	while(max(c) > 0):
		solution += reduceCase(c)
	return ' '.join(solution)

def solve(fin, fout):
	L = codejam_io.read_simple_2(fin, int)
	S = map(solve_case, L)
	codejam_io.write_simple(fout, S)

#solve("A-sample.in", "A-sample.out")
#solve("A-small-attempt0.in", "A-small-attempt0.out")
#solve("A-small-attempt1.in", "A-small-attempt1.out")
#solve("A-small-attempt2.in", "A-small-attempt2.out")
solve("A-large.in", "A-large.out")