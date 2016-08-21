import sys,math

def base(i,b):
    if i == 0: return 0
    s = 0
    p = 1
    while i:
        if i % 10 == 1:
            s = s + p
        
        i //= 10
	p*=b
    return s

def prim(n):
	i = 2
	while i < long(math.sqrt(n))+1:
		if n%i == 0:
			return i
		i+=1
	return 1

if __name__ == '__main__':
	rb = open(sys.argv[1],'r')
	wb = open(sys.argv[2],'w')
	n = int(rb.readline().strip())
	for i in range(1, n+1):
		no = rb.readline().split()
		size = int(no[0])
		n = int(no[1])
		found = 0
		wb.write('Case #'+str(i)+':\n')
		j = long(math.pow(2,size - 1))
		while True:
			j+=1
			if j%2 == 0:
				continue
			number = '{0:b}'.format(j)
			bad = False
			div = []
			for b in range(2,11):
				copy = int(number)
				nb = base(copy,b)
				d = prim(nb)
				if d == 1:
					bad = True
					break
				div.append(str(d))
			if bad == False:
				found += 1
				wb.write(number + ' '+ ' '.join(div) + '\n')
			if found == n:
				break
		
	rb.close()
	wb.close()
