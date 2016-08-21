import sys

def get_ans(s):

	cnt = 0 


	if len(s) == 1:
		if s == '+':
			return 0
		if s == '-':
			return 1

	s = list(s)

	while True:
		if '-' not in s:
			break

		st = s[0]
		reach = 1

		# print st
		for j in range(1,len(s)):

			if st != s[j]:
				break
			reach += 1



		for j in range(reach):
			if s[j] == '+' : s[j] = '-'
			elif s[j] == '-' : s[j] = '+'

		# print s
		# raw_input()
		cnt += 1

	return cnt

# f = open("A-large.in" , "r")
f = open("B-large.in" , "r")

lines = f.readlines()

N = int(lines[0])

for i in range(N):
	s = lines[i+1].split("\n")[0]
	ans = get_ans(s)

	ans = "Case #"+str(i+1)+": "+str(ans)
	print ans