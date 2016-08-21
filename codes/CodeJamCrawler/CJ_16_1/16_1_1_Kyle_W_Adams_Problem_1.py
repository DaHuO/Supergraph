
def lastWord(letters):
	result = letters[0]
	for c in letters[1:]:
		if result[0] > c:
			result += c
		else:
			result = c + result
	return result

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n = input()
  print("Case #{}: {}".format(i, lastWord(n)))
  # check out .format's specification for more formatting options