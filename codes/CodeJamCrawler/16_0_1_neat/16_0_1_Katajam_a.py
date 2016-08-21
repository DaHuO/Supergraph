def getNum(x):
	return list(map(int, list(str(x))))

def solution(ori, x, num, used):
	if x in used: return 'INSOMNIA'
	for i in getNum(x):
		num.add(i)

	if num == SLEEP: return x
	used.add(x)
	x += ori
	return solution(ori, x, num, used)

SLEEP = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

n = int(input())
for i in range(n):
	data = int(input())
	num = set([])
	used = set([])
	ori = data
	print("Case #{}: {}".format(i+1, solution(ori, data, num, used)))
