# your code goes here
import sys
T=int(input())
num=T
for k in range(0,num):

	K,C,S = map(int,sys.stdin.readline().split())
	print("Case #",end="")
	print(k+1,end=": ")
	for i in range(0,K,1):
		if i!=K-1:
			temp=i*pow(K,C-1)+1
			print(temp,end=" ")
		else:
			temp=i*pow(K,C-1)+1
			print(temp)
			