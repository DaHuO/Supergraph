import sys

count = 0

def resetCount():
	global count
	count = 0

def incCount():
	global count
	count = count + 1

def flip(stack, index):
	bottom = stack[index:]
	top = stack[:index]
	top.reverse()
	
	incCount()

        return map(lambda x: '-' if x is '+' else '+', top) + bottom
		

def setFrontForFlip(stack):
        j = 1
        while j < len(stack)  and stack[j] is '+':
            j = j + 1
	return flip(stack, j)

def checkFront(stack):
	for cake in stack:
		if cake is '-':
			return False
	return True

def minFlips(stack):
	length = len(stack)
	cakes = list(stack)

	for i in range(length-1, -1, -1):
		if cakes[i] is '-':

                        if cakes[0] is '+':
                            cakes = setFrontForFlip(cakes)

			if checkFront(cakes) is False:
				cakes = flip(cakes, i+1)
			else:
				return cakes
	return cakes

def main():
	with open(sys.argv[1], 'r') as file, open('out', 'w') as out:
		data = file.read().split()
		T  = int(data.pop(0))
		
		for i in range(T):
			resetCount()
			stack = data.pop(0)
			minFlips(stack)
			out.write("Case #" + str(i+1) + ": " + str(count) + "\n")
main()
