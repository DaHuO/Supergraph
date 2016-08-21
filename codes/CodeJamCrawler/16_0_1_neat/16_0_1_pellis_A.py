import numpy as np

filename = 'AL'
fin = open(filename+'.in', 'r')
fout = open(filename+'.out', 'w')

for i in range(int(fin.readline().strip())):
	tmp = fin.readline().strip().split(' ')
	N = int(tmp[0])
	num = 0
	nums = [False]*10
	cont = (N != 0)
	while cont:
		num += N
		for d in str(num):
			nums[int(d)] = True
		cont = not np.all(nums)
	res = 'Case #'+str(i+1)+': '+('INSOMNIA' if num == 0 else str(num))+'\n'
	fout.write(res)
	print (res)
		
fout.close()
fin.close()