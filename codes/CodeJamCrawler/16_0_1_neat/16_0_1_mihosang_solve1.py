class Sheep:
	def __init__(self):
		self.sheep = set()
	def process(self,data):
		self.output = data
		self.sheep.update([int(x) for x in str(self.output)])
		for i in range(100):
			self.sheep.update([int(x) for x in str(self.output)])
			if len(self.sheep) == 10:
				return self.output
			else:
				self.output += data
		return 'INSOMNIA'
if __name__ == '__main__':
  T = int(raw_input())
  for i in range(1,T+1):
		N = int(raw_input())
		sheep = Sheep()
		output = sheep.process(N)
		print 'Case #%d: %s' % (i,output)
