# Uses https://github.com/DarioFanucchi/CompetitionCode.git
import sys
sys.path.insert(0, "../../../CompetitionCode")
import codejam_io

def greedy_1(P):
	if 0 not in P:
		return 0
	else:
		return 1 + greedy_1([1-z for z in P[:len(P)-P[::-1].index(0)]])


def fromBase(s, b):
	return sum(int(d)*b**i for i,d in enumerate(s[::-1]))


def solve_case(x):
	(K,C,S) = x
	solns = [[t-1 if t <= K else 0 for t in range(i, i+C)] for i in xrange(1, K+1, C)]
	if len(solns) <= S:
		return ' '.join(map(str, [1+fromBase(x, K) for x in solns]))
	else:
		return 'IMPOSSIBLE'


def solve(fin, fout):
	L = codejam_io.read_simple(fin)
	S = map(solve_case, L)
	codejam_io.write_simple(fout, S)

#solve("D-sample.in", "D-sample.out")
#solve("D-small-attempt0.in", "D-small-attempt0.out")
solve("D-large.in", "D-large.out")