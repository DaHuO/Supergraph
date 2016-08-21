# -*- UTF-8 -*-

if __name__ == "__main__":
	T = int(input())
	for t in range(T):
		pancakes = input()
		turns = 0
		pancake_side = pancakes[0]
		if pancake_side == '-':
			turns += 1
		for pancake in pancakes[1:]:
			if pancake_side != pancake:
				if pancake == '-':
					turns += 2
			pancake_side = pancake
		print ('Case #' + str(t+1) + ': ' + str(turns))