# -*- coding: utf-8 -*-

def solve():
	N, J = map(int,input().split())
	x = (1<<(N-1))+1
	cnt = 0
	ans = [0 for i in range(10)]
	for i in range((1<<(N-2))):
		y = i*2+x
		num = 0
		out = 0
		for u in range(2,11):
			z = 0
			Y = y
			rank = 1;
			while Y > 0:
				if Y%2 == 1:
					z = z+rank
				Y = (Y>>1)
				rank = rank*u
			if u == 10:
				out = z
			for j in range(2,z):
				if j*j > z or j > 100:
					break
				if z%j == 0:
					ans[u-1] = j
					num = num+1
					break
			if num != u-1:
				break
		if num == 9:
			cnt = cnt+1
			print(out,end="")
			for j in range(1,10):
				print(" ",end="")
				print(ans[j],end="")
			print()
		if cnt == J:
			break

T = int(input())
print("Case #1:")
solve()

