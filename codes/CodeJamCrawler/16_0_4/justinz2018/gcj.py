import sys
sys.stdin = open("D-small-attempt0.in","r")
sys.stdout = open("out.txt","w")
n = int(input())
for i in range(n):
	t = list(map(int, input().split()))
	num = t[0]**(t[1]-1)
	n = 0
	print("Case #{}: ".format(i+1), end='')
	for j in range(t[0]):
		print(n+1, end=' ')
		n += num
	print()

