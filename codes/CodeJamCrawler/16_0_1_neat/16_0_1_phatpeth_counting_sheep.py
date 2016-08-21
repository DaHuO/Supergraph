case = int(input())
ans = ""
for i in range(case):
	N = int(input())
	if N == 0:
		ans += ("Case #"+str(i+1)+": INSOMNIA\n")
		continue
	temp = "0123456789"
	T = 0
	while temp != "":
		T += 1
		for c in str(N*T):
			temp = temp.replace(c,"")
	ans += ("Case #"+str(i+1)+": "+str(N*T)+"\n")
print(ans)
	