t = int(input())

for test in range(1, t + 1):
	visited = [0,1,2,3,4,5,6,7,8,9]
	n = int(input())	
	i = 1
	while(1):
		if(n == 0):
			print("Case #" + str(test) + ": INSOMNIA")
			break
		

		sam = i * n

		while(sam != 0):
			t = sam % 10
			if(visited[t] != -1):
				visited[t] = -1
			sam = sam // 10

		if(sum(visited) == -10):
			print("Case #" + str(test) + ": " + str(i * n))
			break

		i += 1



