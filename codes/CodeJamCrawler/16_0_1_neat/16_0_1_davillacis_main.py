import sys
import time


class InputReader:
	def __init__(self, filepath):
		try:
			sys.setrecursionlimit(10000)
			f = open(filepath)
			contents = f.readlines()
			f.close()
			T = contents.pop(0)
			with open('output.out', 'w') as fout:
				count = 1
				while len(contents) > 0:
					print '***************'
					print 'TEST ' + str(len(contents))
					N = contents.pop(0).rstrip()
					pr = Problem(N)
					print pr.toString()

					t = time.time()
					res = pr.solve()
					elapsed = time.time() - t
					print res, elapsed
					print '\n\n\n'
					fout.write('Case #'+str(count)+': '+str(res)+'\n')
					count += 1

			fout.close()
		except TypeError as e:
			print e
		except IOError as e:
			print e
		except NameError as e:
			print e
		except AttributeError as e:
			print e
		except:
			print "Unexpected error:", sys.exc_info()[0]


class Problem:
	def __init__(self, N):
		self.N = N
		self.lista_principal = []
		self.maxnum = 0

	def solve(self):
		try:
			ret = 'INSOMNIA'
			if self.extractList(self.N, self.lista_principal, 1):
				ret = self.maxnum

			return ret

		except TypeError as e:
			print e
		except NameError as e:
			print e
		except AttributeError as e:
			print e
		except KeyError as e:
			print e
		except RuntimeError as e:
			print e
		except:
			print "Unexpected error:", sys.exc_info()[0]

	def toString(self):
		print 'N: ' + str(self.N)

	def extractList(self, number, lista_principal, index):
		int_n = int(number)*(index)
		self.maxnum = int_n
		lista = map(int, list(str(int_n)))
		for n in lista:
			if n not in lista_principal:
				lista_principal.append(n)

		if len(lista_principal) < 10:
			if sorted(list(number)) == sorted(list(str(int_n*(index+1)))):
				return False
			self.extractList(number, lista_principal, index+1)

		return True


if __name__ == '__main__':
	#ir = InputReader('sample.in')
	ir = InputReader('/Users/david/Downloads/A-large.in')