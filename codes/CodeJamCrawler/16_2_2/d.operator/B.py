# Uses https://github.com/DarioFanucchi/CompetitionCode.git
import sys
sys.path.insert(0, "../../../CompetitionCode")
import codejam_io

def padLeft(d, n):
	d1 = str(d)
	return'0'*max(0, n-len(d1)) + d1

def repInline(s, sub):
	s1 = [ch for ch in s]
	sidx = 0
	for idx,ch in enumerate(s):
		if ch == '?':
			s1[idx] = sub[sidx]
			sidx += 1
	return ''.join(s1)

def solve_small(c):
	coders = c[0]
	jammers = c[1]
	x = coders.count('?')
	y = jammers.count('?')
	bestDist = 10**20
	bestCoders = ''
	bestJammers = ''
	for i in xrange(10**x):
		for j in xrange(10**y):
			curC = repInline(coders, padLeft(i, x))
			curJ = repInline(jammers, padLeft(j, y))
			A = int(curC)
			B = int(curJ)
			if(abs(A-B) < bestDist):
				bestDist = abs(A-B)
				bestCoders = curC
				bestJammers = curJ
	return ' '.join([bestCoders, bestJammers])


def solve_case(c):
	return solve_small(c)

def solve(fin, fout):
	L = codejam_io.read_simple(fin, str)
	S = map(solve_case, L)
	codejam_io.write_simple(fout, S)

#solve("B-sample.in", "B-sample.out")
solve("B-small-attempt0.in", "B-small-attempt0.out")
#solve("B-small-attempt1.in", "B-small-attempt1.out")
#solve("B-small-attempt2.in", "B-small-attempt2.out")
#solve("B-large.in", "B-large.out")