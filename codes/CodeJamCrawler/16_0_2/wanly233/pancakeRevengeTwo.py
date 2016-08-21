import sys

class Solution(object):
	def simplify(self, s):
		ret, curr = s[0], s[0]
		for i in range(1, len(s)):
			if s[i] != curr:
				ret += s[i]
				curr = s[i]
		return ret

	def pancakeRevenge(self, s):
		curr = self.simplify(s)
		count = 0
		while curr != '+':
			temp = ''
			if curr[0] == '+': temp = '-' + curr[1:]
			else: temp = '+' + curr[1:]
			curr = self.simplify(temp)
			count += 1
		return count

# s = Solution()
# print s.pancakeRevenge('--+-')

out = open("res.out", 'w')
args = []
with open("B-large.in") as f:
    lines = f.readlines()[1:]
    for line in lines:
    	args.append(line.strip())

for i in range(len(args)):
	obj = Solution()
	res = obj.pancakeRevenge(args[i])
	# print res
	out.write("Case #{}: {}\n".format(i + 1, res))