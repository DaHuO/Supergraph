import sys

rl = lambda: map(int, raw_input().split())

def main():
	t = int(raw_input())  # read a line with a single integer
	for i in xrange(1, t + 1):
		S = str(raw_input())
		l = list(S)

		theList = []

		while True:
			if not delNum(l,'Z','ZERO'):
				break
			else:
				theList.append(0)
		while True:
			if not delNum(l,'W','TWO'):
				break
			else:
				theList.append(2)
		while True:
			if not delNum(l,'U','FOUR'):
				break
			else:
				theList.append(4)
		while True:
			if not delNum(l,'X','SIX'):
				break
			else:
				theList.append(6)
		while True:
			if not delNum(l,'G','EIGHT'):
				break
			else:
				theList.append(8)
		while True:
			if not delNum(l,'O','ONE'):
				break
			else:
				theList.append(1)
		while True:
			if not delNum(l,'F','FIVE'):
				break
			else:
				theList.append(5)
		while True:
			if not delNum(l,'R','THREE'):
				break
			else:
				theList.append(3)
		while True:
			if not delNum(l,'V','SEVEN'):
				break
			else:
				theList.append(7)
		while True:
			if not delNum(l,'N','NINE'):
				break
			else:
				theList.append(9)


		print "Case #{}: {}".format(i, "".join(map(str,sorted(theList))))
		# check out .format's specification for more formatting options

def delNum(l,ch,numStr):
	try:
		ind = l.index(ch)
		for c in numStr:
			del(l[l.index(c)])
		return True
	except ValueError:
		return False

def delZero(l):
	try:
		ind = l.index("Z")
		for c in "ZERO":
			del(l[l.index(c)])
		return True
	except ValueError:
		return False

def delSix(l):
	try:
		ind = l.index("X")
		for c in "SIX":
			del(l[l.index(c)])
		return True
	except ValueError:
		return False

def delTwo(l):
	try:
		ind = l.index("W")
		for c in "TWO":
			del(l[l.index(c)])
		return True
	except ValueError:
		return False

def delFour(l):
	try:
		ind = l.index("U")
		for c in "FOUR":
			del(l[l.index(c)])
		return True
	except ValueError:
		return False

def delEight(l):
	try:
		ind = l.index("G")
		for c in "EIGHT":
			del(l[l.index(c)])
		return True
	except ValueError:
		return False

def delFive(l):
	try:
		ind = l.index("F")
		for c in "FIVE":
			del(l[l.index(c)])
		return True
	except ValueError:
		return False

def delThree(l):
	try:
		ind = l.index("R")
		for c in "THREE":
			del(l[l.index(c)])
		return True
	except ValueError:
		return False

# def delSix(l):


main()