f = open("input.txt", "r")
lines = f.readlines()
f.close()
f = open("result.txt", "w")



def generate(lst, word, current):
	if len(current) == len(word):
		lst.append(current)
	elif word[len(current)] == "?":
		for i in range(10):
			generate(lst, word, current + str(i))
	else:
		generate(lst, word, current + word[len(current)])

for i in range(1, len(lines)):
	line = lines[i]
	word1 = line.split()[0]
	word2 = line.split()[1]
	words1 = []
	words2 = []
	generate(words1, word1, "")
	generate(words2, word2, "")
	mindiff = 1000
	result = ""
	for c in words1:
		for j in words2:
			if abs(int(c)-int(j)) < mindiff:
				mindiff = abs(int(c)-int(j))
				result = c + " " + j
	f.write("Case #" + str(i) + ": " + result + "\n")
f.close()
