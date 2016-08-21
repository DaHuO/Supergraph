T = int(input())

for i in range(T):

	n = input()
	s = set(n)
	num = cont = int(n)

	if cont == cont + num:
		r = "INSOMNIA"

	else:
		while len(s) < 10:
			cont += num			
			s.update(set(str(cont)))

		r = str(cont)

	print("Case #",i+1,": ",r,sep="")