#part a
import sys
sys.stdin = open('A-small-attempt0.in', 'r')
sys.stdout = open('output.out', 'w')

for i in xrange(1, input()+1):
	nums = set()
	temp = num = input()
	for j in xrange(1, 100000):
		for k in str(temp):
			nums.add(k)
		if len(nums) >= 10:
			print "Case #%d: %d"%(i, temp)
			break
		temp+=num
	else:
		print "Case #%d: INSOMNIA"%i
