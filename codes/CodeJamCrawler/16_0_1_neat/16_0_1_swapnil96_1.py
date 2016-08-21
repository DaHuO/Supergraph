from math import pow
class count:

	def __init__(self, bo):

		self.bo = bo

	def total(self):

		no = self.bo
		length = len(no)
		array = []
		j = 1

		while len(array) != 10 and j <= pow(10, 7): 
			
			lo = str(int(no)*j)

			if lo == no and j != 1:
				return 'INSOMNIA'
				break

			temp = [0]*len(lo)

			for i in range(0, len(lo)):
				temp[i] = lo[i]

			temp = sorted(set(temp))
			temp = map(int, temp)
			
			for x in range(0, len(temp)):
				array.append(temp[x])
			
			array = sorted(set(array))
			j += 1

		if len(array) == 10:
			return lo	
		
		elif j > pow(10, 7):
			return 'INSOMNIA'

a = int(raw_input())
que = []*a

for i in range(0,a):
	
	y = raw_input()
	que.append(y)

sol = []*a

for h in range(0, a):

	q = count(que[h])
	sol.append(q.total())

fo = open('foo2.txt', 'w')

for  g in range(0, a):	
	fo.write("Case #%d: %s \n" % (g+1, sol[g]))







