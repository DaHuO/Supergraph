T = int(input())
num = [0,1,2,3,4,5,6,7,8,9]
last = 0
for i in range(1,T + 1):
	N = input()
	count = 1
	while len(num) > 0:
		if int(N) == 0:
			last = "INSOMNIA"
			break
		for j in str(int(N) * count):
			if int(j) in num:
				num.remove(int(j))
		count += 1
		last = int(N) * count - int(N)
	print("Case #{0}: {1}".format(i,last))
	num = [0,1,2,3,4,5,6,7,8,9]

