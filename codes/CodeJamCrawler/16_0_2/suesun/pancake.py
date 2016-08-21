import sys
N = int(sys.stdin.readline().strip())
def decide(listPack):
	if len(listPack) == 0:
		return 0
	listPackL = []
	if listPack[-1] == -1:
		for number in listPack[:-1]:
			listPackL.append(-number)
		return 1+decide(listPackL)
	else:
		return decide(listPack[:-1])


for qw in range(1,N+1):
	s = sys.stdin.readline().strip()
	listPack = []
	for char in s:
		if char == '-':
			listPack.append(-1)
		else:
			listPack.append(1)

	print("Case #%d: %d"%(qw,decide(listPack)))