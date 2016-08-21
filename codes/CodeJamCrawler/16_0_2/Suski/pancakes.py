import sys

def makeArray(pancakeString):
	pancakes = []
	numPancakes = len(pancakeString)
	for i in range (numPancakes):
		pancakes.append(pancakeString[i])
	return pancakes

def flippedBottom(pancakes):
	for i in reversed (pancakes):
		if i == '+':
			pancakes.pop()
		else:
			return

def flipStack(pancakes):
	numPancakes = len(pancakes)
	end = numPancakes -1
	for i in range (numPancakes):
		if i > end - i:
			return
		if i == end -i:
			if pancakes[i] == '-':
				pancakes[i] = '+'
			else:
				pancakes[i] = '-'
			return
		temp = pancakes[i]
		if pancakes[end-i] == '-':
			pancakes[i] = '+'
		else:
			pancakes[i] = '-'
		if temp == '+':
			pancakes[end-i] = '-'
		else:
			pancakes[end-i] = '+'


def flipTop(pancakes):
	numPancakes = len(pancakes)
	for i in range (numPancakes):
		if pancakes[i] == '+':
			pancakes[i] = '-'
		else:
			return



def process(fin):
	pancakes = makeArray(fin.readline().rstrip())
	flippedBottom(pancakes)
	flips = 0
	while len(pancakes) > 0:
		if pancakes[0] == '-':
			flipStack(pancakes)
		else:
			flipTop(pancakes)
		flips +=1
		flippedBottom(pancakes)

	return flips

def main():
    input_name = sys.argv[1]
    fin = open(input_name, 'r')

    num_cases = int (fin.readline())
    for i in range(num_cases):
        result = process(fin)
        print("Case #{}: {}".format((i+1), result))

if __name__ == '__main__':
    main()