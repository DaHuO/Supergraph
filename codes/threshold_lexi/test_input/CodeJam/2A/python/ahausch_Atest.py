import sys

cmb = {
 'P' : 'PR',
 'S' : 'PS',
 'R' : 'RS'
};

solutions = dict()

for result in ['P', 'S', 'R']:	
	key = (result.count('R'),result.count('P'),result.count('S'))
	solutions[key] = result
		
	for i in range(13):
		next = ''

		for r in result:
			next += cmb[r];
			
		result = next;
			
		key = (result.count('R'), result.count('P'),result.count('S'))
		solutions[key] = result;

def treesort(str):
	if len(str) > 1:
		mid = len(str) // 2
		a = treesort(str[mid:])
		b = treesort(str[:mid])
		
		if a < b:
			return a + b
		return b + a
	return str

fin = open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin

T = int(fin.readline())

for t in range(1, T + 1):
	N, R, P, S = map(int, fin.readline().split(' '))
	
	key = (R, P, S)
	if key in solutions:
		str = solutions[key]
		
		print("Case #{}: {} ".format(t, treesort(str)))
	else:
		print("Case #{}: IMPOSSIBLE".format(t))
