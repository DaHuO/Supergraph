
def maneuver(ss):
	S1 = ss.replace('+','*')
	S2 = S1.replace('-','+')
	S3 = S2.replace('*','-')
	return S3[::-1]

def minMan(S):
	if len(S) == 0:
		return 0

	if S.endswith('+'):
		return minMan(S.rstrip('+'))

	if S.startswith('-'):
		return 1 + minMan( maneuver(S.lstrip('-')) )

	if S.startswith('+'):
		return 2 + minMan( maneuver(S.lstrip('+').lstrip('-')) )



if __name__ == "__main__":
	T = input()
	 
	for case in xrange(1, T+1):
		S = raw_input()
		#print("Case #%i: %s" % (caseNr, solve(cipher)))
		print "Case #%i: %s" % (case, minMan(S))