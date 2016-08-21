T = int(input())  # read a line with a single integer

for i in range(1, T + 1):
	S = input()
	J = S[0]
	for j in range(1, len(S)):
		if(S[j]>=J[0]):
			J = S[j]+J
		else:
			J = J+S[j]
	print("Case #{}: ".format(i),J)
	