
import time

def fallAsleep(N, i, list):
	if N == 0:
		return "INSOMNIA"
	elif len(list) == 0:
		return N * (i - 1)
	else:
		return fallAsleep(N, i+1, countSheep( N*i, list))

def countSheep (bigN, remainingSheep):
	newSheeps = [int(i) for i in str(bigN)]
	for x in newSheeps:
		if x in remainingSheep:
			remainingSheep.remove(x)
	return remainingSheep

start_time = time.time()
# f = open("sample.txt")
f = open("A-small-attempt1.in")
f = open("A-large.in")
result = open('A-large.in-output.txt', 'w')

cases = int(f.readline().rstrip())
for x in xrange(0, cases):
	N = int(f.readline().rstrip())
	caseResult = "Case #"+str(x+1)+": " + str(fallAsleep(N, 1, range(10))) + "\n"
	result.write(caseResult)
f.close()
result.close()
print("--- %s seconds ---" % (time.time() - start_time))
