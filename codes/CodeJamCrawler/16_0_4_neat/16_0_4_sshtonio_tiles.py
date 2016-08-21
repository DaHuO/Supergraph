
def fct(K, C, pos):
	prev = pos - 1
	for i in range(1,C):
		prev = prev*K + pos - 1
	return prev+1

nb_entry = int(input())
for i in range(1,nb_entry+1):
	out = "Case #"+str(i)+': '
	[K, C, S] = map(int, raw_input().split())

	l  = range(1,K+1)
	if C==1:
		s = ' '.join(map(str,l))
		out += (s,"IMPOSSIBLE")[K>S]
		print(out)
		continue

	l2 = [fct(K,C,j) for j in l]
	s = ' '.join(map(str,l2))
	out += s
	print(out)
	
	
