T = input()
for t in range(1,T+1):
	N = input()
	arr=[]
	for n in range(0, N*2-1):
		arr.append(raw_input().split(' '))
	d={}
	for i in range(0,len(arr)):
		for j in range(0, len(arr[i])):
			if arr[i][j] in d:
				d[arr[i][j]]+=1
			else:
				d[arr[i][j]]=1
	ans = []
	for key in d:
		if not d[key]%2==0:
			ans.append(int(key))

	ans.sort()

	print "Case #" + str(t) + ": " + ' '.join(str(x) for x in ans)