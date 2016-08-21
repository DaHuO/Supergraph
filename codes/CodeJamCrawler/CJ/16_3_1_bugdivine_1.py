def resolve(arr, total, l):
	k = 0
	while (total > 0):
		arr.sort(key=lambda y:y[0], reverse=True)
		if (total == 1):
			print arr[k][1],
			total-=1
		elif (total-2.0 == 0):
			arr[k][0] -= 1
			if (arr[k][0] == 0):
				k+=1
			arr[k][0] -= 1
			print arr[k-1][1]+arr[k][1],
			total-=2
		elif (arr[l][0]/(total-2.0) <= 0.5):
			arr[k][0] -= 1
			arr[k+1][0] -= 1
			print arr[k][1]+arr[k+1][1],
			total-=1
			total -= 1
			while arr[k][0] == 0:
				l -= 1
				del arr[k]
		elif (arr[l][0]/(total-1.0) <= 0.5):
			arr[k][0] -= 1
			print arr[k][1],
			total -= 1
			while arr[k][0] == 0:
				l -= 1
				del arr[k]
		else:
			arr[k][0] -= 1
			if ((arr[l][0]-1)/(total-2.0) <= 0.5):
				total-=1
				arr[k+1][0] -= 1
				print arr[k][1]+arr[k+1][1],
			else:
				print arr[k][1],
			while arr[k][0] == 0:
				l -= 1
				del arr[k]
				pass
			total-=1


t = int(input())
for _t in range(t):
	x = int(input())
	k = 0
	arr = [[int(a)] for a in raw_input().split()]
	total = 0
	for a in range(x):
		total += arr[a][0]
		arr[a].append(chr(a+ord('A')))
	arr.sort(key=lambda y:y[0], reverse=True)
	print 'Case #'+str(_t+1)+':',
	resolve(arr, total, x-1)
	print
