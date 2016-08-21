def all_happy(pancakes):
	return len(pancakes) == pancakes.count(1)

def flip(pancakes, i):
	for j in range(i, len(pancakes)):
		if pancakes[j] == 0:
			pancakes[j] = 1
		else:
			pancakes[j] = 0

T = int(input())
for i in range(T):
	pancakes = input()
	L = []
	for pancake in pancakes:
		if pancake == '-':
			L.append(0)
		else:
			L.append(1)
	L.reverse()
	moves = 0
	while not all_happy(L):
		flip(L, L.index(0))
		moves += 1
	print("Case #{}: {}".format(i + 1, moves))