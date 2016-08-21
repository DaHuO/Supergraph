import sys

T = int(raw_input())

NUM_STRS = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

chr2num = {}
for i in range(len(NUM_STRS)):
	s = NUM_STRS[i]
	for c in s:
		if c in chr2num: chr2num[c].append(i)
		else: chr2num[c] = [i]

chr2num_one = dict([ (k,v[0]) for k,v in chr2num.items() if len(v) == 1 ])
 
#print chr2num
#print chr2num_one

def removeChrs(str, num):
	str = list(str)
	for c in NUM_STRS[num]:
		if c not in str:
			return -1
		str.remove(c)
	return str

def searchNum(str):
	#print str
	c = str[0]
	ret = []
	for n in chr2num[c]:
		new_str = removeChrs(str, n)
		if new_str == -1:
			continue
		if len(new_str) == 0:
			return [n]

		se_ret = searchNum(new_str)
		if len(se_ret) > 0 : 
			return se_ret + [n]

	return ret

for t in range(1, T+1):
	S = list(raw_input())
	#print S

	nums = []

	for c in chr2num_one:
		if c in S:
			num = chr2num_one[c]
			nums.append(num)
			S = removeChrs(S, num)
		if not S: break

	if S:
		nums = nums + searchNum(S)

	nums = sorted(nums)
	num = ''.join(map(str, nums))

	print 'Case #%d: %s' % (t, num)
