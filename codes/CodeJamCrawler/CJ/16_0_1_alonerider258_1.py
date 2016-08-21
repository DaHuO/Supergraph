def check(l):

	count = 0
	num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
	for d in l:
		if(d in num):
			num.remove(d)
			
	if (len(num) == 0): 
		return True

	return False
	

def main():

	f = open('input.txt', 'r')
	tc = int(f.readline())
	t = 0
	r = open('output.txt', 'w')

	while (tc > 0): 
		l = []	
		n = int(f.readline())
		p = n
		i = 0
		t = t+1

		while (True):
			if p == 0 : 
				k = "Case #" + str(t) + ':' + ' INSOMNIA' + '\n'
				r.write(k)
				break

			strn = str(n)
			for d in strn:
				if (int(d) not in l):
					l.append (int(d))


			if (check(l)):
				k = "Case #" + str(t) + ': ' + str(n) + '\n'
				r.write(k)
				break

			i = i + 1
			n = i*p
		tc -= 1

main()
