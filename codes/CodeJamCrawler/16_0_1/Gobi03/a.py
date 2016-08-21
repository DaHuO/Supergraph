error = "INSOMNIA"
dp = [False]*10

n = int(input())

def fillDP(num):
	if num == 0:
		()
	else:
		if not dp[num%10]:
			dp[num%10] = True
		fillDP(num // 10)

def check():
	for b in dp:
		if not b:
			return False
	return True

def resetDP():
	for i in range(10):
		dp[i] = False

for i in range(n):
	now = int(input())
	ans = -1
	if now == 0:
		ans = error
	else:
		cnt = 0
		while cnt < int(9e18):
			cnt += now
			fillDP(cnt)
			if check():
				ans = cnt
				resetDP()
				break

	print("Case #",i+1,": ", ans,sep = "")
