f = open("A-large.in", "r")
new_file = open("last_wordLargeOut", "w")
t = int(f.readline())

def solver(word):
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	last_word = []
	for letter in word:
		if last_word == []:
			last_word.append(letter)
		else:
			if alphabet.find(letter) >= alphabet.find(last_word[0]):
				last_word.insert(0,letter)
			else:
				last_word.append(letter)
	return "".join(last_word)


for i in range(1,t+1):
	word = f.readline()[:-1]
	last_word = solver(word)
	new_file.write("Case #"+str(i)+ ": "+last_word+"\n")
