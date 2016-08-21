from sets import Set
import time


t = input()
for tc in range(t):
	n  = input()
	print 'Case #{}:'.format(tc+1),

	if n==0:
		print 'INSOMNIA'
		continue

	name = n
	digitsSet = set(list(str(name)))
	while len(digitsSet) != 10:
		name += n
		# print set(list(str(name)))
		digitsSet = digitsSet.union(set(list(str(name))))
		# print digitsSet
		# time.sleep(1)

	print name

