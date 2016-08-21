import sys

def solve(s):
	word = s[:1]
	for ch in s[1:]:
		if ch >= word[0]:
			word = [ch] + word
		else:
			word.append(ch)
	return ''.join(word)

def main():
	n = int(raw_input())
	for i in xrange(n):
		s = list(raw_input())
		word = solve(s)

		print 'Case #{}: {}'.format(i + 1, word)


if __name__ == '__main__':
	main()