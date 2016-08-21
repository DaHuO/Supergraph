import itertools

file = open("/Users/daviddai/Desktop/in.txt", "r")
data = file.read()
file.close()

data = data.split('\n')[1:]
opt = ''

data.reverse()

#TODO
case = 1
while data:
	dpop = data.pop()
	if dpop:
		N = int(dpop.strip())

		hs = {}
		for i in range(2*N - 1):
			nums = data.pop().split()
			for i in nums:
				if int(i) not in hs:
					hs[int(i)] = 1
				else:
					hs[int(i)] += 1
		oddNum = []
		allNum = set()

		for k, v in hs.items():
			allNum.add(k)
			if v % 2:
				oddNum.append(k)

		oddNum.sort()

		if len(oddNum) == N:
			raw = ''
			for e in oddNum:
				raw += (' ' + str(e))
			opt += "Case #" + str(case) + ":" + raw + '\n'
		else:
			raw = ''
			possible = list(itertools.combinations(allNum, N - oddNum))
			for p in possible:
				for num in p:
					oddNum.append(num)
			oddNum.sort()
			for e in oddNum:
				raw += (' ' + str(e))
			opt += "Case #" + str(case) + ":" + raw + '\n'
		case += 1

file = open('result.txt', 'w')
file.write(opt)
file.close()




