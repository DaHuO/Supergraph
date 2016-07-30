import itertools
import string

beats = {"P": "R", "R": "S", "S": "P"}
loses_to = {b: a for (a,b) in beats.items()}


solns = {}
for winner in "PRS":
    okStrings = [winner]
    for N in range(3):
        print N
        print "{} current acceptable strings".format(len(okStrings))
        newOkStrings = []
        for okString in okStrings:
            lists = itertools.product(*[((p, beats[p]), (beats[p], p)) for p in okString])
            for list in lists:
                newOkStrings.append("".join(["".join(pair) for pair in list]))

        okStrings = sorted(newOkStrings)
        best = okStrings[0]
        P, R, S = best.count("P"), best.count("R"), best.count("S")
        solns[(N+1, P, R, S)] = best

for key in sorted(solns.keys()):
    print key, solns[key]

def solve(N,R,P,S):
    return solns.get((N,P,R,S), "IMPOSSIBLE")

def test(inputs, ans):
	b = solve(*inputs)
	if (b != ans):
		print "Failed test! Inputs {} should give answer of {} not {}".format(' '.join(inputs), ans, b)

def main():

    outfile = open('a.out','w')
    T = int(string.strip(raw_input()))    

    for k in xrange(1,T+1):
        print k
        N, R, P, S = map(int,string.strip(raw_input()).split())
        answer = solve(N, R, P, S) # add appropriate arguments
        outfile.write('Case #%d: %s\n' % (k,answer))

if __name__ == '__main__':
    main()
    pass