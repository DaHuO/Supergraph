import sys
sys.stdout = open("outputC.out", 'w')

N = 16
J = 50
case = 1

arr = [0 for i in xrange(N-2)]
def factor(num):
	if num%2:
		for i in xrange(3, int(num**0.5)+1, 2):
			if num%i == 0:
				return i
		else:
			return 1
	else:
		return 2
def genNum(pos=0):
	global case 
	if pos < N-2:
		# Case its 0
		arr[pos] = 0
		genNum(pos+1)

		# Case its 1
		arr[pos] = 1
		genNum(pos+1)
	elif case <= J:
		s = "1" + "".join(map(str, arr)) + "1"
		lst = [factor(int(s, i)) for i in xrange(2, 11)]
		if all(map(lambda a:a!=1, lst)):
			print "%s %s"%(s, " ".join(map(str, lst)))
			case += 1
print "Case #1:"
genNum()