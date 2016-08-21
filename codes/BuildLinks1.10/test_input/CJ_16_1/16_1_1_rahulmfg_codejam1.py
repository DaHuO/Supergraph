#! usr/bin/python

f = open("A-large.in")


noc = int(f.readline())

case = 1
if noc <= 100:
	for word in f:
		lastword = ''
		for w in word:
			if lastword == '':
				lastword = w
			elif ord(lastword[0]) < ord(w):
				lastword = w + lastword
			elif ord(lastword[0]) > ord(w):
				lastword = lastword + w
			else:
				lastword = w + lastword
		lastword = lastword.replace('\n','')
		print 'Case #%d: %s' % (case, lastword)
		case += 1