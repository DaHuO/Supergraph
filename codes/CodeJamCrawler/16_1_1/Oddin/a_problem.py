#!/usr/bin/python
import sys

cases = int(sys.stdin.readline().rstrip("\n"),10)


for c in range(0,cases):
	answer=""
	word=sys.stdin.readline().rstrip("\n")
	l_word=[]
	for a in word:
		l_word.append(a)
	first_letter=l_word[0]
	answer=first_letter

	for alpha in l_word[1:]:
		if answer[0]<=alpha:
			answer=alpha+answer
		else:
			answer=answer+alpha
		first_letter=alpha

		

	print("Case #"+str(c+1)+": "+answer)
