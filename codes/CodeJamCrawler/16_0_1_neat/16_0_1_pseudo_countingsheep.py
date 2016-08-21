import sys

inputfile = open(sys.argv[1],'r')
outputfile = open(sys.argv[1].replace("in","out"), 'w')

testcases = int(inputfile.readline())
#print visitlist
for i in range(0, testcases):
		N = int(inputfile.readline())
		if(N == 0):
				outputfile.write("Case #" + str(i+1) + ": INSOMNIA\n")
				continue
		visitlist = [False] * 10
		final = N
		j=1
		while False in visitlist:
				final = N * j
				n_str = str(final)
				for c in n_str:
						visitlist[int(c)]=True
#				print visitlist
#				print final 
				j = j + 1
		outputfile.write("Case #" + str(i+1) + ": " + str(final) + "\n")
