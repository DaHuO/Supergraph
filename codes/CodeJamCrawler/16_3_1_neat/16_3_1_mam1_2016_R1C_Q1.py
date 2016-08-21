#MAM, Google Code Jam - 2016 Round 1C, Problem 1
#senators
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def countSens(sens, seno):
	answer = 0
	for ch in seno:
		answer = answer + sens[ch]
	return answer

def solve(N, senators):
	answer = ""
	sendict = dict()

	for x in xrange(len(senators)):
		sendict[alphabet[x]] = senators[x]

	senorder = sorted(sendict, key = sendict.get, reverse = True)

	if N == 2:
		return " AB" * sendict["A"]

	while (sendict[senorder[0]] > 1):
		sendict[senorder[0]] = sendict[senorder[0]] - 1
		answer = answer + " " + senorder[0]
		senorder = sorted(sendict, key = sendict.get, reverse = True)

	for each in senorder[:-2]:
		answer = answer + " " + each
	answer = answer + " " + senorder[-2] + senorder[-1]

	return answer

def main():
	with open('A-large.in', 'r') as infile, open('output.txt', 'w') as outfile:
		
		T = int(infile.readline())
		for x in xrange(T):
			N = int(infile.readline())
			line = [int(z) for z in infile.readline().rstrip().split(" ")]
			outfile.write("Case #" + str(x + 1) + ":" + str(solve(N, line)) + "\n")

if __name__ == "__main__":
	main()