import Queue
from heapq import heappop, heappush, heapify, nlargest

T = input()

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Party(object):

	def __init__(self, name, count):
		self.name = name
		self.count = count

	def __cmp__(self, other):
		return cmp(other.count, self.count)

	def __str__(self):
		return '[{0}:{1}]'.format(self.name, self.count)

	def __repre__(self):
		return self.__str__()

def print_list(a):
	for x in a:
		print x,
	print ''

def solve():
	N = input()
	X = map(int, raw_input().split())
	#q = Queue.PriorityQueue()
	q = []
	parties = []
	left = 0
	for i in xrange(len(X)):
		p = Party(letters[i], X[i])
		# q.put(p)
		heappush(q, p)
		parties.append(p)
		left += X[i]

	ans = ''
	while len(q) > 0:
#		print q
		# p1 = q.get()
		p1 = heappop(q)
		# print 'p1 ::: ', p1
		left -= 1
		p1.count = p1.count - 1
		if p1.count > 0:
			# q.put(p1)
			heappush(q, p1)
		ans += p1.name
		# print_list(parties)
		# print 'left ---> ', left
		if left == 1:
			x = heappop(q)
			# print 'test ::: ----> ', x
			heappush(q, x)

		#try one more
		if len(q) > 0:
			# p2 = q.get()
			p2 = heappop(q)
			# print 'p2 ::: ', p2

			if left == 1:
				ans += p2.name
				continue

			p2.count -= 1
			if p2.count > 0:
				# q.put(p2)
				heappush(q, p2)
			# print_list(parties)
			# p3 = q.get()
			p3 = None
			if len(q) > 0:
				p3 = heappop(q)
			# print 'p3 ::: ', p3
			# print 'left ---> ', left
			if not p3 or p3.count <= (left - 1)/2:
				left -= 1
				# q.put(p3)
				ans += p2.name
				# print 'used p2'
			else:
				p2.count += 1
				if p2.count == 1:
					heappush(q, p2)
				# print 'put p2 back'
			if p3:
				heappush(q, p3)
			# print_list(parties)

		ans += ' '
	return ans
	# print '==='*10


for t in range(T):
    print 'Case #{0}: {1}'.format(t+1, solve())
