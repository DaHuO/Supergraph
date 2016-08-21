from collections import defaultdict

with open('in.txt','rb') as fin, open('output.txt','w') as fout:
	case = 1

	it = iter(fin.readlines())
	_ = next(it)

	for line in it:
		print ("\n\n\n")
		print ("case " + str(case))
		
		line = [c for c in list(line) if c=='+' or c=='-']
		n=0
		clast='+'
		for c in reversed(line):
			if c!=clast:
				n+=1
			clast=c

		fout.write("Case #" + str(case) + ": " + str(n) + "\n")
		case += 1