# Uses https://github.com/DarioFanucchi/CompetitionCode.git
import sys
sys.path.insert(0, "../../../CompetitionCode")
import codejam_io

def extractDigits(lst, slst, phase):
	digits = []
	for p1 in phase.keys():
		n1 = phase[p1]
		while(lst[ord(p1)-65] > 0):			
			for ch in slst[n1]:
				lst[ord(ch)-65] -= 1
			digits.append(n1)
	return digits


def solve_case(s):
	s = s[0]
	slst = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
	lst = [0 for i in xrange(26)]
	for ch in s:
		lst[ord(ch)-65] += 1

	phase1 = {"G":8, "Z":0, "U":4, "W":2, "X":6}
	phase2 = {"F":5, "H":3, "O":1, "S":7}

	digits = []
	digits.extend(extractDigits(lst, slst, phase1))
	digits.extend(extractDigits(lst, slst, phase2))
	digits.extend([9]*lst[ord("I")-65])

	return ''.join(map(str, sorted(digits)))

def solve(fin, fout):
	L = codejam_io.read_simple(fin, str)
	S = map(solve_case, L)
	codejam_io.write_simple(fout, S)

#solve("A-sample.in", "A-sample.out")
#solve("A-small-attempt0.in", "A-small-attempt0.out")
#solve("A-small-attempt1.in", "A-small-attempt1.out")
#solve("A-small-attempt2.in", "A-small-attempt2.out")
solve("A-large.in", "A-large.out")