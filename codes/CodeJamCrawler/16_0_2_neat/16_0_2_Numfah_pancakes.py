def swap(state):
	if state == '+':
		return '-'
	else:
		return '+'

def flip(pancakes):
	return ''.join(map(swap, pancakes[::-1]))

def happy_pancakes(pancakes):
	index = len(pancakes) - 1
	count = 0

	while index >= 0:
		if pancakes[index] == '+':
			index -= 1
		else:
			count += 1
			if pancakes[0] == '-':
			#flip under bottom most -
				pancakes = flip(pancakes[:index+1]) + pancakes[index+1:]
			else:
			#flip above first - in bottom most batch
				while pancakes[index] == '-':
					index -= 1
				pancakes = flip(pancakes[:index+1]) + pancakes[index+1:]
	return count

def main():
	f = open('pancakes_input.txt', 'r')
	output = open('pancakes_output.txt', 'w')
	T = f.readline()
	for i in range(1,int(T)+1):
		pancakes = str(f.readline()).rstrip()
		number = happy_pancakes(pancakes)
		# print number
		output.write("Case #%d: %d\n" %(i, number))
	f.close()
	output.close()