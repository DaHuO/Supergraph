from sys import stdin, setrecursionlimit
setrecursionlimit(2000)
cin = lambda: stdin.readline().strip('\n\r ')

t = int(cin())
data = [cin() for i in range(t)]

def find_max(s):
	word = s[0]
	s = s[1:]
	
	for ch in s:
		if ch >= word[0]:
			word = ch + word
		else:
			word += ch
	
	return word

for i in range(t):
	s = data[i]
	print "Case #%i: %s" % (i + 1, find_max(s))