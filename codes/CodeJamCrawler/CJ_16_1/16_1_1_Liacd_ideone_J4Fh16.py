T = int(input())

for i in range(T):

	word = iter(list(input()))

	r = next(word)
	
	for letter in word:
		if letter >= r[0]:
			r = letter + r
		else:
			r += letter

	print("Case #",i+1,": ",r,sep="")