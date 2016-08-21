from collections import Counter

T = int(input())


for i in range(T):

	n = 2 * int(input()) -1
	
	r = []
	f = []

	for j in range(n):
		r.extend(input().split())

	for n,o in Counter(r).items():
		if o % 2 == 1:
			f.append(n)

	print("Case #",i+1,": "," ".join(sorted(f)),sep="")