digits=("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE")
digits=("ONE","NINE")

"""z=0
w=2
x=6
g=8
u=4 > f=5/r=3 > v=7


o/i=9
"""

for c in xrange(1,input()+1):
	S = list(raw_input().strip())
	
	num = []
	
	while S.count("Z") != 0:
		S.remove("Z")
		S.remove("E")
		S.remove("R")
		S.remove("O")
		num.append("0")
		
	while S.count("W") != 0:
		S.remove("T")
		S.remove("W")
		S.remove("O")
		num.append("2")
		
	while S.count("X") != 0:
		S.remove("S")
		S.remove("I")
		S.remove("X")
		num.append("6")
		
	while S.count("G") != 0:
		S.remove("E")
		S.remove("I")
		S.remove("G")
		S.remove("H")
		S.remove("T")
		num.append("8")
		
	while S.count("U") != 0:
		S.remove("F")
		S.remove("O")
		S.remove("U")
		S.remove("R")
		num.append("4")
		
	while S.count("F") != 0:
		S.remove("F")
		S.remove("I")
		S.remove("V")
		S.remove("E")
		num.append("5")
		
	while S.count("V") != 0:
		S.remove("S")
		S.remove("E")
		S.remove("V")
		S.remove("E")
		S.remove("N")
		num.append("7")
		
	while S.count("R") != 0:
		S.remove("T")
		S.remove("H")
		S.remove("R")
		S.remove("E")
		S.remove("E")
		num.append("3")
		
	while S.count("O") != 0:
		S.remove("O")
		S.remove("N")
		S.remove("E")
		num.append("1")
		
	while S.count("I") != 0:
		S.remove("N")
		S.remove("I")
		S.remove("N")
		S.remove("E")
		num.append("9")
	
	num.sort()
	print "Case #%d: %s" % (c,"".join(num))