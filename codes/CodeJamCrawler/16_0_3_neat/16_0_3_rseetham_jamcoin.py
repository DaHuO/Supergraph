import itertools
def jamcoin(n,lines):
	a = list(itertools.product([0,1], repeat=n))
	count = 0
	output = ''
	for comb in a :
		if (comb[0] == 1) and (comb[n-1] == 1) :
			case = ''
			case = case.join(map(str,comb))
			case = case + ' '
			flag = 0
			for i in range(2,11) :
				val = 0
				k = 0
				for j in range(n-1,-1,-1) :
					val = val + (comb[j] * (i ** k))
					k = k + 1
				div = divisor(val)
				if div == 0 :
					break
				case = case + str(div) + ' '
				if i == 10 :
					output = output + case + '\n'
					#print (output)
					count = count + 1
					if count == lines :
						return output

def divisor(val) :
	for i in range (2, int(val ** 0.5) + 1) :
		if val % i == 0 :
			return i
	return 0

if __name__ == '__main__':
	try :
		t = int(input())
		for i in range(1, t + 1):
			n, j = [int(s) for s in input().split(" ")]
			print("Case #%i: \n%s" % (i, jamcoin(n,j)))
	except EOFError:
		print ("Error: EOF or empty input!")