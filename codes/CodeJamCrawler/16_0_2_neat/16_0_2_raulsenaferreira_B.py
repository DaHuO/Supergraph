import sys

T = int(input())

for t in range(0,T):
	prev=''
	pancakes=input()
	cont=0

	for p in pancakes:
		if p!=prev:
			cont+=1
			prev=p
	if prev=='+':
		print("Case #{}: {}".format(t+1, cont-1))
	else:
		print("Case #{}: {}".format(t+1, cont))
