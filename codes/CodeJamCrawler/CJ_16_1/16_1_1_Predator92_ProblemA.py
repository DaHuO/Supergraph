def problemA():
	string = raw_input()
	word = []
	last_letter_w = 0
	first_letter_w = 0
	# print string
	for char in string:
		weight = get_letter_weight(char)
		# print weight
		if not word:
			word.append(char)
			continue
		last_letter_w = get_letter_weight(word[-1])
		first_letter_w = get_letter_weight(word[0])
		# print first_letter_w, last_letter_w
		if weight >= first_letter_w:
			word = [char] + word
		else: 
			word.append(char)

		# print word
	return ''.join(word)

def get_letter_weight(char):
	if char is None:
		return -1
	return ord(char) - ord('A')

if __name__ == '__main__':
	T = int(raw_input())
	case = 1
	while T>0:
		print "Case #%s: %s" % (case, problemA())
		case = case + 1
		T = T - 1