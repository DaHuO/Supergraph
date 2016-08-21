def epilogue(result, num):
	out_file.write("Case #" + str(num+1) + ": " + result + '\n')

in_file, out_file = open('A-large.in', 'r'), open('A-large.out', 'w')

num_cases = int(in_file.readline())
for case_num in range(num_cases):
	S = in_file.readline()
	if S[-1] == '\n':
		S = S[:-1]
	new_word = [S[0]]
	for i in range(1, len(S)):
		if S[i] >= new_word[0]:
			new_word.insert(0, S[i])
		else:
			new_word.append(S[i])
	new_word = "".join(new_word)
	epilogue(new_word, case_num)
