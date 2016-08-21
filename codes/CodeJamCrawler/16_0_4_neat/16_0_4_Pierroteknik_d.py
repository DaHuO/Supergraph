T = int(input())
for t in range(T):
	K, C, S = list(map(int,input().split()))
	li = []
	Dep = int((K**C)/S) - 1
	for i in range(S):
		li.append((i+1)+i*(Dep))
	print("Case #" + str(t+1) + ":",end="")
	for i in li:
		print(" " + str(i),end="")
	print("")