import sys

def solve(stream):
	s = stream.readline().strip()
	answer = s[0]
	for i in range(1, len(s)):
		if s[i] < answer[0]:
			answer += s[i]
		else:
			answer = s[i] + answer
	return answer

if __name__ == "__main__":
	input = sys.argv[1]
	file = open(input, "r")
	T = int(file.readline().strip())
	for t in range(T):
		result = solve(file)
		print(("Case #%d: %s") % (t + 1, result))
	file.close()
