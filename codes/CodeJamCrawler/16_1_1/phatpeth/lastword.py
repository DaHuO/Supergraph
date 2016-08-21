T = int(input())
ans = ""
for i in range(T):
	S = input()
	head = S[0]
	combi = head
	first = 1
	for c in S:
		if first == 1:
			first = 0
			continue
		else:
			if c >= head:
				combi = c+combi
				head = c
			else:
				combi += c
	ans += ("Case #"+str(i+1)+": "+combi)
	if i != T-1:
		ans += "\n"
print(ans)
	