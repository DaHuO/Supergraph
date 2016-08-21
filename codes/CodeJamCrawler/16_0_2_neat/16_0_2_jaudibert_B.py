
def count_flips(s):
	transitions = 0
	curr = s[0]
	for c in s[1:]:
		if c != curr:
			transitions += 1
			curr = c
	if s[-1] == "-":
		return transitions + 1
	return transitions

def main():
	# take in input
	t = int(raw_input())

	solutions = []

	for i in range (t):
		s = raw_input()
		solutions.append("Case #" + str(i+1) + ": " + str(count_flips(s)))

	for solution in solutions:
		print solution


if __name__ == "__main__":
	main()