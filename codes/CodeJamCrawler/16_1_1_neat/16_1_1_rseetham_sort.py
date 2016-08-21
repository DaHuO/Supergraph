def sort(s) :
	s = list(s)
	p = s[0]
	o = p	
	for i in range(1,len(s)) :
		if  p <= s[i] :
			o = s[i]+o
			p = s[i]
		else :
			o = o + s[i]
	return o

if __name__ == '__main__':
	try :
		t = int(input())
		for i in range(1, t + 1):
			s = input()
			print("Case #%i: %s" % (i, sort(s)))
	except EOFError:
		print ("Error: EOF or empty input!")