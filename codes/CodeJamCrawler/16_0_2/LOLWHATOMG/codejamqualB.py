#part b
import sys
#
sys.stdin = open('B-large.in', 'r')
sys.stdout = open('outputB.out', 'w')

# 0 for +
# 1 for -
for testCase in xrange(1, input()+1):
	cakes = raw_input()
	dp = [[0 for i in xrange(len(cakes))] for j in xrange(2)]

	if cakes[0] == "+":
		dp[1][0] = 1
	elif cakes[0] == "-":
		dp[0][0] = 1

	for i in xrange(1, len(cakes)):
		if cakes[i] == "+":
			#_+ -> ++
			dp[0][i] = min(dp[0][i-1], dp[1][i-1] + 1)
			#_+ -> --
			dp[1][i] = min(dp[0][i-1] + 1,	dp[1][i-1] + 2)
		elif cakes[i] == "-":
			#_- -> ++
			dp[0][i] = min(dp[0][i-1] + 2, dp[1][i-1] + 1)
			#_- -> --
			dp[1][i] = min(dp[0][i-1] + 1, dp[1][i-1])
	print "Case #%d: %d"%(testCase, min(dp[0][len(cakes)-1], dp[1][len(cakes)-1]+1))
