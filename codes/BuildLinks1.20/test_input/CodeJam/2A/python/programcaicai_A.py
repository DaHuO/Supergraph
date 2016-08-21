
order = 'RPSR'

from collections import Counter

def solve(N,R,P,S):


	base_sol = ['R','P','S']
	def g(s):
		mp = {'R':'RS','P':'PR','S':'PS'}
		return ''.join(mp[c] for c in s)

	
	for _ in range(N):
		for i in range(3):
			base_sol[i] = g(base_sol[i])



	def my_sort(s):
		if len(s)==1:
			return s
		else:
			A = s[:len(s)//2]
			B = s[len(s)//2:]
			if A<B:
				return my_sort(A) + my_sort(B)
			else:
				return my_sort(B) + my_sort(A)



	for i in range(3):

		d = Counter(base_sol[i])
		d2 = {'R':R,'P':P,'S':S}
		if all(d2[k] == v for k,v in d.items()):
			return my_sort(base_sol[i])
	return 'IMPOSSIBLE'


T = int(input())

for casno in range(T):
	N,R,P,S = [int(x) for x in input().split()]
	result = solve(N,R,P,S)


	print('Case #{}: {}'.format(casno+1,result))
