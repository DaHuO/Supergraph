from collections import defaultdict

with open('in.txt','rb') as fin, open('output.txt','w') as fout:
	case = 1

	it = iter(fin.readlines())
	_ = next(it)

	for line in it:
		print ("case " + str(case))
		N = int(line)
		if N==0:
			result = "INSOMNIA"
		else:
			k=N
			g=set(['0','1','2','3','4','5','6','7','8','9'])
			while len(g)!=0:
				g-=set(str(k))
				result = k
				k+=N

		fout.write("Case #" + str(case) + ": " + str(result) + "\n")
		case += 1