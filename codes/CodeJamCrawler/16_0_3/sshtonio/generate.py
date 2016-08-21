nb_entry = int(input())

def prime(n):
	for i in range(2,int(n**0.5)+1):
		if n%i==0:
			return [False, i]
		if i>100000:
			return [True, 0]
	return [True, 0]

for i in range(1, nb_entry+1):
	out = "Case #"+str(i)+':\n'
	[N, J] = map(int, input().split())

	nbcoin = 0

	for k in range(2**(N-2)):
		mid = bin(k)[2:]
		coin = '1'+'0'*(N-2-len(mid))+mid+'1'
		l = [ int(coin, j) for j in range(2,11)]
		
		ldiviseur = []
		b = False
		for isitprime in l:
			[b, d] = prime(isitprime)
			if b:
				break
			else:
				ldiviseur.append(d)
		if b:
			continue
		else:
			out+=coin+' '+' '.join(map(str,ldiviseur))+'\n'
			nbcoin +=1
		
		if nbcoin == J:
			print(out)
			break
