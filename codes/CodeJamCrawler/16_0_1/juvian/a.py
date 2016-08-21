
st = ""

with open("a.in","a+") as f:
	lines = f.read().split("\n")

lineCount = int(lines[0])

for line in range(1,lineCount+1):

	n = int(lines[line])

	copy = n

	seen = set(str(n))

	answ = 1

	if len(seen) == 10 or n == 0:
		answ = 1
	else:
		for x in xrange(1,1000):
			copy+=n
			seen = seen | set(str(copy))
			if(len(seen)) == 10:
				answ = x+1
				break

	if(len(seen) < 10):
		st+= "Case #"+str(line)+": INSOMNIA\n"
	else:
		st+= "Case #"+str(line)+": "+str(answ*n)+"\n"			


with open("a.out","w+") as f:
	f.write(st)		