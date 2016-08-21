from itertools import permutations, chain, combinations

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def length(LC):
	for subset in list(powerset(LC))[::-1]:
		for permutation in permutations(subset):
			for index, element in enumerate(permutation):
				bff = F[element]
				if permutation[index-1] != bff and permutation[(index+1) % len(permutation)] != bff:
					break
			else:
				return len(permutation)

T = int(input())

for t in range(1, T+1):

	N = int(input())
	F = list(map(int, input().split()))
	F = [0] + F
	LC = list(range(1, N+1))	

	print("Case #{}: {}".format(t, length(LC)))
