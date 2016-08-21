t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
	s = raw_input()
	s = s.lower()
	alphabetic = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	lastWord = ""
	for j in xrange(0, len(s)):
		if (lastWord == ""):
			lastWord = str(s[j])
			continue
		if (alphabetic.index(str(s[j])) >= alphabetic.index(str(lastWord[0]))):
			lastWord =  str(s[j]) + lastWord
		else:
			lastWord = lastWord + str(s[j]) 
	print("Case #{}: {}".format(i, lastWord.upper()))			