from collections import defaultdict

freqs = defaultdict(set)
words = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
for word in words:
	for letter in word:
		freqs[letter].add(word)

#print freqs

for t in range(int(raw_input())):
	S = raw_input()
	result_str = []

	list_of_tuples = []
	for l in S:
		list_of_tuples.append((l, len(freqs[l])))

	list_of_tuples.sort(key=lambda tup: tup[1])

	#print list_of_tuples

	for letter, length in list_of_tuples:
		#print S
		if S != "":
			possible_words = freqs[letter]
			for word in possible_words:
				if all(l in S for l in word):
					result_str.append(word)
					for l in word:
						S = S.replace(l, "", 1)
					break


	result = [words.index(s) for s in result_str]

	result.sort()

	res = ""
	for n in result:
		res += str(n)

	print "Case #{}: {}".format(t+1, res)