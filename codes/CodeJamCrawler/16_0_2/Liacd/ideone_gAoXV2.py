T = int(input())

for i in range(T):

	n = input()
	f = n[0]
	r = 0

	for l in n:
		if l != f:
			r += 1
		f = l
	
	if n[-1] == "-":
		r += 1

	print("Case #",i+1,": ",r,sep="")