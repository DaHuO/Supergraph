#!/usr/bin/python

import sys

def addchars(b,l,i,dic):
	"""
		>>> addchars(0,0,1,{})
		INSOMNIA
		>>> addchars(1,1,1,{})
		10
		>>> addchars(1692,1692,1,{})
		5076
	"""
	if b == 0:
		return "INSOMNIA"

	for c in str(l):
		if c not in dic:
			dic[c]=True

			if len(dic)==10:
				return l

	return addchars(b,b*(i+1),i+1,dic)


def main():
	inputFile = sys.argv[1]
	# inputFile = "./p1-input"
	f = open(inputFile)

	for i in xrange(0,int(f.readline())):
		line = f.readline()
		print "Case #"+str(i+1)+":",addchars(long(line),long(line),1,{})
	

if __name__ == "__main__":
    import doctest
    # doctest.testmod()
    main()



