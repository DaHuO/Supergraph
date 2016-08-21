import re
cases = raw_input()
case = int(cases)
	


for i  in range(case):
	nb = raw_input()
	number = str(nb)
	nsol = 0
	aa = i+1
	inpu = re.sub(r'([+-])\1{1,}', r'\1', number)
	if inpu[len(inpu)-1] == "+":
		print "Case #"+str(aa)+": "+str(len(inpu)-1)
	else:		
		print "Case #"+str(aa)+": "+str(len(inpu))

