# /usr/bin/env python3

from collections import defaultdict

WORDS = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def get_number(counts):
	# print_counts(counts)
	if counts_is_empty(counts):
		return ''
	for i, word in enumerate(WORDS):
		word_counts = get_counts(word)
		try:
			return str(i) + get_number(sub_counts(counts, word_counts))
		except:
			pass

	raise Exception()

def counts_is_empty(counts):
	for k, v in counts.items():
		if v > 0:
			return False
	return True

def get_counts(s):
	counts = defaultdict(lambda: 0)
	for c in s:
		counts[c] += 1
	return counts

def counts_contains(a, b):
	for k, v in b.items():
		if a[k] < v:
			return False
	return True

def sub_counts(a, b):
	if not counts_contains(a, b):
		raise Exception()
	result = get_counts('')
	for k, v in a.items():
		result[k] = v - b[k]
	return result

def print_counts(counts):
	s = ''
	for k, v in counts.items():
		s += str(v) + k + ' '
	print(s)


T = int(input())

for case_number in range(T):
	case_string = "Case #" + str(case_number + 1) + ":"
	s = input()
	number = get_number(get_counts(s))
	print(case_string, number)

# print(counts_contains(get_counts('aabc'), get_counts('abc')))
# print_counts(sub_counts(get_counts('aabc'), get_counts('abc')))
# print(counts_contains(get_counts('aabc'), get_counts('abcc')))
# print_counts(sub_counts(get_counts('aabc'), get_counts('abcc')))

# print('number:', get_number(get_counts('ONE')))
# print('number:', get_number(get_counts('ONETWOTHREE')))
# print('number:', get_number(get_counts('SIXSEVENFIVENINEFIVENINEEIGHT')))
