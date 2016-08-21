import sys
sys.stdin = open('input.in', 'r')
sys.stdout = open('output.out', 'w')
t = int(input())
for k in range(t):
	n = int(input())
	if n == 0:
		print('case #', k+1, ': ', 'INSOMNIA', sep = '')
		continue
	s = set()
	i=1
	while len(s) < 10:
		s=s.union(set(list(str(n*i))))
		i+=1
	print('case #', k+1, ': ', n*(i-1), sep ='')