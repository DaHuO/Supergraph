def flip(s):
	l = []
	for i in xrange(len(s)):
		if s[i] == '-':
			l.append('+')
		else:
			l.append('-')
	temp = ''.join(l)
	return temp

# Outline
# Check for negative pancakes at the top of the stack.
# 	- If there are any flip them
# Find the negative pancake that is the lowest in the stack
# Flip the stack which has the above pancake at its lowest
# Repeat until there are no neg pancakes left

T = int(raw_input().strip())
for i in xrange(1,T+1):
	S = raw_input().strip()
	steps = 0
	while True:
		if S[0] == '+':
			begin_index = 0
			while begin_index < len(S) and S[begin_index] == '+':
				begin_index += 1
			if begin_index == len(S):
				break
			else:
				t = S[:begin_index][::-1]
				S = flip(t) + S[begin_index:]
				steps += 1
		end_index = len(S)-1
		while end_index >= 0 and S[end_index] == '+':
			end_index -= 1
		if end_index == -1:
			break
		else:
			t = S[:end_index+1][::-1]
			S = flip(t) + S[end_index+1:]
			steps += 1
	print "Case #" + str(i) + ": " + str(steps)