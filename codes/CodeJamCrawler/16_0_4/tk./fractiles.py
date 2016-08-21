import sys
import sympy.ntheory
import itertools

# WARNING: Assumes all input is squeaky clean.

def main():
	T = int(sys.stdin.readline())

	for case_num in range(1,T+1):
		input_line = sys.stdin.readline()
		args = input_line.split(' ')
		K = int(args[0])
		C = int(args[1])
		S = int(args[2])

		U = dummy_solution(K, C)

		print("Case #{0}:".format(case_num)),
		if len(U) > S:
			print("IMPOSSIBLE")
		else:
			for u in U:
				print(u),
			print('')
			
def dummy_solution(K, C):
	return set([i*(K**(C-1))+1 for i in range(K)])

def tiles_to_uncover(K, C):
	pass

def grow_pattern(K, C):
	fractals = []
	patterns = itertools.product("GL", repeat=K)
	for pattern in patterns:
		fractal = ''.join(pattern)
		for i in range(C):
			new_fractal = []
			for c in fractal:
				if c == "L":
					new_fractal.append(''.join(pattern))
				elif c == "G":
					new_fractal.append("G"*len(pattern))
			fractal = ''.join(new_fractal)
		fractals.append(fractal)
	return fractals

if __name__ == "__main__":
	main()