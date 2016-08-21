def solve(string):
	answer = string[0]
	for i in string[1:]:
		if i>=answer[0]:
			answer = i+answer
		else:
			answer += i
	return answer

ip = open('A-small.in')
op = open('A-small.out', 'w')
n = int(ip.readline().strip())
for i in range(n):
	string = ip.readline().strip()
	op.write('Case #'+str(i+1)+': '+solve(string)+'\n')
ip.close()
op.close()
