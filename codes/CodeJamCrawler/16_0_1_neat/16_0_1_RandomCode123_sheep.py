t=int(raw_input())

for r in xrange(1, t + 1):
  input = raw_input()
  foundnumbers = []
  lastdigit=0
  d=1
  while len(foundnumbers) is not 10:
	n=int(input)*d
	if n<1:
		lastdigit="INSOMNIA"
		break
	lastdigit=n
	s= str(n)
	nlist = []
	for i in s:
		nlist.append(int(i))
	for i in nlist:
		if i not in foundnumbers:
			foundnumbers.append(i)
			foundnumbers.sort()
	d+=1
  print "Case #{}: {}".format(r, lastdigit)