with open("A-large.in") as f:
	content = f.readlines()

T = int(content[0])
N = content[1:]
print N

fs = open("output.txt", 'wb')

alldigits = [0,1,2,3,4,5,6,7,8,9]
currdigit = []
if T<1 or T>=101:
	print "Number of tests Constraints not met exiting..."
else:
	for i in xrange(0,T):
		if int(N[i])>=0 and int(N[i])<=1000000:
			if int(N[i]) == 0:
				print "Case #" + str(i+1) + ": INSOMNIA"
				fs.write("Case #" + str(i+1) + ": INSOMNIA" + "\n")
			else:
				iteration = 1
				currdigit = []
				remaindigit = set(alldigits) - set(currdigit)
				remaindigit = list(remaindigit)
				while remaindigit:
					value = int(N[i]) * iteration
					strval = str(value)
					for j in strval:
						# print j
						currdigit.append(int(j))
						# print currdigit

					iteration += 1
					remaindigit = set(alldigits) - set(currdigit)
					remaindigit = list(remaindigit)

				print "Case #" + str(i+1) + ": " + str(value)
				fs.write("Case #" + str(i+1) + ": " + str(value) + "\n")
		else:
			print "Constraints not met moving on to next case..."

fs.close()