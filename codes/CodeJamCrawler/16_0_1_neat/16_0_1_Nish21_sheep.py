for t in range(int(input())):
	visited = [False]*10
	x = int(input())
	x1 = x
	if x == 0:
		print("Case #"+str(t+1)+": INSOMNIA")
		continue
	temp=0
	while(not all(visited)):
		temp = x;
		while(int(temp) > 0):
			visited[int(temp%10)]=True
			temp /= 10
		x+=x1
	print("Case #"+str(t+1)+": " + str(x-x1))
