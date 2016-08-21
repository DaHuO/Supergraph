import os
mi = [1,2,4,8,16,32,64,128,256,512]
n = int(input())
for i in range(1, n+1):
	m = input()
	tem = int(m)
	sor = tem
	flag = 0
	if m is '0':
		print("Case #{}: {}".format(i, "INSOMNIA"))
	else:
		while 1:
			a = list(str(tem))
			for k in a:
				flag = flag | mi[int(k)]
				#print(flag)
				if flag == 1023:
					print("Case #{}: {}".format(i, tem))
					break
			if flag == 1023:
				break
			tem = tem + sor
			#print(tem)
