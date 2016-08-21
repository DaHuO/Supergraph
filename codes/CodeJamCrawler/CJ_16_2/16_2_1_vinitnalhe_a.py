m = 10**6 + 1
from collections import Counter
def solve(s):
	cnt = Counter(s)
	arr = [0]*10
	arr[0] = cnt['Z']
	arr[2] = cnt['W']
	arr[4] = cnt['U']
	arr[6] = cnt['X']
	arr[8] = cnt['G']
	arr[1] = cnt['O'] - arr[2] - arr[4] - arr[0]
	arr[3] = cnt['T'] - arr[2] - arr[8]
	arr[5] = cnt['F'] - arr[4]
	arr[7] = cnt['V'] - arr[5]
	arr[9] = cnt['I'] - arr[5] - arr[8] - arr[6]
	ans = ''
	# print arr
	for i in range(10):
		if arr[i] != 0:
			ans += str(i)*arr[i]
	return ans

t = int(raw_input())
for caseNr in xrange(1, t+1):
	s = raw_input()

	print("Case #%i: %s" % (caseNr, solve(s)))







