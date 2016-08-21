#!/usr/bin/python
import sys
# any + at the right side can be ignored and removed
# --+-
# +-++ = +-
# --
# ++

# -- filip
# + remove
# +- filip 1 -- filip ++


# +----- => +++++- => ------ => ++++++


def flip(s):
	"""
	>>> flip("+++-")
	'---+'
	>>> flip("+")
	'-'
	>>> flip("+-+-")
	'-+-+'
	"""
	s = s.replace("+","n")
	s = s.replace("-","+")
	s = s.replace("n","-")
	return s

def getMinNumberOfFlips(s,i):
	if s=='+':
		return i;
	if s=='-':
		return i+1
	if s[-1]=="+":
		return getMinNumberOfFlips(s[:-1],i)
	elif s[-2:]=="--":
		s = flip(s)
		return getMinNumberOfFlips(s,i+1)
	else:
		#+-
		temp = flip(s[:-1])
		s = temp + s[-1]
		s = flip(s)
		return getMinNumberOfFlips(s,i+2)


def main():
	inputFile = sys.argv[1]
	# inputFile = "./p1-input"
	f = open(inputFile)

	for i in xrange(0,int(f.readline())):
		line = f.readline()
		print "Case #"+str(i+1)+":",getMinNumberOfFlips(str(line).rstrip(),0)
	

if __name__ == "__main__":
    import doctest
    # doctest.testmod()
    main()



