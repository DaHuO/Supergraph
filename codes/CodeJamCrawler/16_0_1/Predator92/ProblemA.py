
def problemA():
	dic_num = {}
	N = int(raw_input())
	n = 0
	while N>0:
		n = n + N
		dic_num = count(dic_num, n)
		if sanity_check(dic_num):
			return n
	return "INSOMNIA"

#False continue serie
#True stop => sleep
def sanity_check(dic_num):
	if len(dic_num) == 10:
		return True
	return False

def count(dic_num, N):
	while N>0:
		num = N % 10
		N = N / 10
		dic_num[str(num)] = True
	return dic_num
 
if __name__ == '__main__':
	T = int(raw_input())
	case = 1
	while T>0:
		print "Case #%s: %s" % (case, problemA())
		case = case + 1
		T = T - 1
 