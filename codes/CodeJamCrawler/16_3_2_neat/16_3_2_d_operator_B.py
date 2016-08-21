# Uses https://github.com/DarioFanucchi/CompetitionCode.git
import sys
sys.path.insert(0, "../../../CompetitionCode")
import codejam_io

def write_slst_h(fname, strlst):
	lwrt = []
	for i, L in enumerate(strlst):
		lwrt.append('Case #' + str(i+1) + ': ' + L[0] + '\n')
		lwrt.extend([' '.join(map(str, s)) + '\n' for s in L[1:]])

	f = open(fname, 'wt')
	f.writelines(lwrt)
	f.close()
	return


def paddedBin(x, L):
	b = bin(x)[2:]
	return '0'*max(L-len(b), 0) + b

def solve_case(c):
	[B, M] = c
	if M > 2**(B-2):
		return ['IMPOSSIBLE']
	elif M == 2**(B-2):
		return ['POSSIBLE',['0' + '1'*(B-1)]] + [['0'*i + '1'*(B-i)] for i in xrange(2,B+1)]
	else:
		return ['POSSIBLE',[paddedBin(M, B-1) + '0']] + [['0'*i + '1'*(B-i)] for i in xrange(2,B+1)] 
		
def solve(fin, fout):
	L = codejam_io.read_simple(fin, int)
	S = map(solve_case, L)
	write_slst_h(fout, S)

#solve("B-sample.in", "B-sample.out")
#solve("B-small-attempt0.in", "B-small-attempt0.out")
#solve("B-small-attempt1.in", "B-small-attempt1.out")
#solve("B-small-attempt2.in", "B-small-attempt2.out")
solve("B-large.in", "B-large.out")