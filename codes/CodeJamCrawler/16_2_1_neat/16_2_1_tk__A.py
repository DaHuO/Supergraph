import sys

# WARNING: Assumes all input is squeaky clean.

def main():
	lettermap = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

	T = int(sys.stdin.readline())

	for case_num in range(1,T+1):
		S = list(sys.stdin.readline().strip())
		phone_digits = []

		while len(S) > 0:
			if 'Z' in S:
				phone_digits.append('0')
				for c in "ZERO":
					S.remove(c)
			elif 'W' in S:
				phone_digits.append('2')
				for c in "TWO":
					S.remove(c)
			elif 'X' in S:
				phone_digits.append('6')
				for c in "SIX":
					S.remove(c)
			elif 'G' in S:
				phone_digits.append('8')
				for c in "EIGHT":
					S.remove(c)
			elif 'U' in S:
				phone_digits.append('4')
				for c in "FOUR":
					S.remove(c)
			else:
				break
		
		# assert that the phone number now only consists of digits 13579
		while len(S) > 0:
			if 'S' in S:
				phone_digits.append('7')
				for c in "SEVEN":
					S.remove(c)
			elif 'T' in S:
				phone_digits.append('3')
				for c in "THREE":
					S.remove(c)
			elif 'F' in S:
				phone_digits.append('5')
				for c in "FIVE":
					S.remove(c)
			elif 'O' in S:
				phone_digits.append('1')
				for c in "ONE":
					S.remove(c)
			else:
				break

		# assert that the phone number now only consists of digits 9
		while len(S) > 0:
			phone_digits.append('9')
			for c in "NINE":
				S.remove(c)

		phone_digits.sort()
		phone_number = ''.join(phone_digits)
		print("Case #{}: {}".format(case_num, phone_number))


if __name__ == "__main__":
	main()