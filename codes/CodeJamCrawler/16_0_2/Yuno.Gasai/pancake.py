def parsePancakes(pancakes):
	#"-" -> 0, "+" -> 1
	def parsePancake(pancake):
		if (pancake=="+"):
			return 1
		return 0
	pile = map(parsePancake, pancakes)
	return pile



def flipPancakes(pile, i):
	#flips the pancakes from the i-th pancake (exclusive)
	flips = pile[:i]
	flips = map(lambda x: x^1, flips)
	flips.reverse()
	pile[:i] = flips


def minFlips(pile):
	#find the first inconsistant number and flip what's before it and flip from there
	flips = 0
	while 0 in pile:
		first = pile[0]
		i = 1
		while i < len(pile) and pile[i]==first:
			i+=1
		if (i<len(pile)):
			flipPancakes(pile, i)
			flips+=1
		else:
			if 0 in pile: #all entries are 0
				flips +=1
			return flips

	return flips








def main():
	fi = open("B-large.in","r")
	T = int(fi.readline())
	fo = open("output.txt","w")
	for i in range(T):
		N = parsePancakes(fi.readline().strip())
		result = minFlips(N)
		fo.write("Case #%i: %s\n"%(i+1,result))
	fi.close()
	fo.close

main()