t=int(input())
case=0
for _ in range(t):
	case+=1
	k,c,s=map(int,input().split())
	print("Case #"+str(case)+":", end=" ")
	for i in range(1,k+1):
		print(str(i),end=" ")
	print()
