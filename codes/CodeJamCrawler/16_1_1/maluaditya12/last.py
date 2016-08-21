#!/usr/bin/env python
t = int(raw_input())
for case in range(t):
	word = raw_input()
	newword = word[0]
	for x in range(1, len(word)):
		if word[x] >= newword[0]:
			newword = word[x] + newword
		else:
			newword = newword + word[x]
	print "Case #{}: {}".format( case +1 , newword)

