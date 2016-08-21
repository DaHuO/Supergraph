from sets import Set
# fin = open("input.txt", "r+")
# fout = open("output.txt", "w")
# T = int(fin.readline())
#print T
T = int(raw_input())
for i in range(T):
	# N = fin.readline()
	#print N
	N = raw_input()
	k = 2
	string = N
	if int(N) == 0:
		print "Case #%d: INSOMNIA" % (i + 1)
		# fout.write("Case #%d: INSOMNIA\n" % (i + 1))
	else:
		data = Set()
		while True:
			for j in range(len(string)):
				ch = string[j]
				if ch not in data:
					data.add(ch)
			if len(data) == 10:
				break
			temp = int(N)
			temp *= k
			k += 1
			string = str(temp)
		print "Case #%d: %s" % ((i + 1), string)
		# fout.write("Case #%d: %s\n" % ((i + 1), string))
# fin.close()
# fout.close()