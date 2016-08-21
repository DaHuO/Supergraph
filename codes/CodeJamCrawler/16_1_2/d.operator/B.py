# Uses https://github.com/DarioFanucchi/CompetitionCode.git
import sys
sys.path.insert(0, "../../../CompetitionCode")
import codejam_io

def solve_case(c):
	c.sort()
	elements = sorted(reduce(lambda a, b: a+b, c))
	uniqueElements = sorted(list(set(elements)))
	counts = {e:0 for e in set(elements)}
	for elt in elements:		
		counts[elt] += 1

	return codejam_io.list_as_string([elt for elt in uniqueElements if counts[elt] % 2 == 1])

def solve(fin, fout):
	L = codejam_io.read_f(fin, lambda x: [int]*(2*x[0]-1))
	S = map(solve_case, L)
	codejam_io.write_simple(fout, S)


#solve("B-sample.in", "B-sample.out")
#solve("B-small-attempt0.in", "B-small-attempt0.out")
#solve("B-small-attempt1.in", "B-small-attempt1.out")
#solve("B-small-attempt2.in", "B-small-attempt2.out")
solve("B-large.in", "B-large.out")