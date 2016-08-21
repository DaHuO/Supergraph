import sys

def get_nums(N):

	k = []
	while N != 0:
		k.append(N%10)
		N = N/10
	return k

def get_ans(N):

	if N == 0:
		return "INSOMNIA"

	cnt = 0
	d = []
	ans = 0
	while True:
		cnt += 1
		nm = cnt * N
		k = get_nums(nm)

		for j in k:
			if j not in d:
				d.append(j)

		d.sort()
		if d == [0,1,2,3,4,5,6,7,8,9]:
			ans = nm
			break


	return ans

f = open("A-large.in" , "r")

lines = f.readlines()

N = int(lines[0])

for i in range(N):
	num = int(lines[i+1])
	ans = get_ans(num)

	ans = "Case #"+str(i+1)+": "+str(ans)
	print ans