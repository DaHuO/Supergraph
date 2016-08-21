from collections import Counter
from itertools import permutations

def isNameInString(name_counter, S_counter):
	for (k,c) in name_counter.items():
		if S_counter[k] < c:
			return False
	return True

def main():
	names = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
	perms = []
	for i in xrange(1,len(names)+1):
		perms.extend(list(permutations(names, i)))
	name_counters = { names[i]: (i, Counter(names[i])) for i in xrange(len(names))}

	for TEST in xrange(1, int(raw_input())+1):
		S = raw_input()
		S_counter = Counter(S)

		phone = []

		for perm in perms:
			S_counter_copy = Counter(S_counter)

			for name in perm:
				(i, name_counter) = name_counters[name]
				while isNameInString(name_counter, S_counter_copy):
					S_counter_copy.subtract(name_counter)
					phone.append(str(i))

			S_counter_copy += Counter()	# remove zero and negative counts
			if len(S_counter_copy) > 0:
				phone = []
			else:
				break

		phone = sorted(phone)
		print "Case #%d: %s" % (TEST, str("".join(phone)))

main()
