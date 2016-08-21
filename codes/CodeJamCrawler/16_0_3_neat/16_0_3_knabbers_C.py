from collections import defaultdict

with open('in.txt','rb') as fin, open('output.txt','w') as fout:
	case = 1

	it = iter(fin.readlines())
	_ = next(it)

	for line in it:
		print ("case " + str(case))
		N,J = [int(s) for s in line.split()]

		r=""
		for j in range(2,11):
			r+=" "+str(j**(N/2)+1)

		fout.write("Case #" + str(case) + ":\n")

		for i in range(J):
			b = ("{0:b}".format(i)).zfill(N/2-2)
			coin = "1"+b+"11"+b+"1"
			fout.write(coin + r + "\n" )

		case += 1