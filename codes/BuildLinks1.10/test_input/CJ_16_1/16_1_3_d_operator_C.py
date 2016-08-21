# Uses https://github.com/DarioFanucchi/CompetitionCode.git
import sys
sys.path.insert(0, "../../../CompetitionCode")
import codejam_io

def getBest(E, visited, cur, prev, start, N):
	if cur == start:
		return N
	if visited[cur]:
		return 0

	visited[cur] = True
	best = 0
	if prev == E[cur]:
		for x in xrange(len(E)):
			v = getBest(E, visited, x, cur, start, N+1)
			if v > best:
				best = v
	else:
		best =  getBest(E, visited, E[cur], cur, start, N+1)		
	visited[cur] = False

	return best


def solve_case(c):
	c = [x - 1 for x in c]
	best = 0
	for i in xrange(len(c)):
		visited = [False]*len(c)
		visited[i] = True
		cur = getBest(c, visited, c[i], i, i, 1)
		if cur > best:
			best = cur
	return best

def solve(fin, fout):
	L = codejam_io.read_simple_2(fin, int)
	S = map(solve_case, L)
	codejam_io.write_simple(fout, S)

#solve("C-sample.in", "C-sample.out")
solve("C-small-attempt0.in", "C-small-attempt0.out")
#solve("C-small-attempt1.in", "C-small-attempt1.out")
#solve("C-small-attempt2.in", "C-small-attempt2.out")
#solve("C-large.in", "C-large.out")