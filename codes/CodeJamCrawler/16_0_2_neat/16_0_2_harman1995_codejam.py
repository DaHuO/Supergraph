from sets import Set

def main():

	N = raw_input()
	N = int(N)
	
	for i in xrange(N):
		s = raw_input()
		s = list(s)
		s1 = []
		prevseen = ''
		for item in s:
			if item != prevseen:
				s1.append(item)
				prevseen = item
		s = s1
		l = len(s)
		ans = 0
		if(s[len(s)-1] == '+'):
			l = len(s)-1
		if(l > 0):
			if(s[0] == '-'):
				l = l-1
				ans = ans+1
		ans += l
		print 'Case #' + str(i+1) + ': ' + str(ans) 

if __name__ == '__main__':
	main()