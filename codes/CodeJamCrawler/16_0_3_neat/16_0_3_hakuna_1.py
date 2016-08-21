def isprime(n):
    if n % 2 == 0:
        return False, 2
    if n % 3 == 0:
        return False, 3

    for f in range(5, int(n ** .5), 6):
        if n % f == 0: 
            return False, f
        if n % (f + 2) == 0:
        	return False, f+2
    return True, n


with open("input.txt", 'r') as infile:
	with open('output.txt', 'w') as f:
		T = int(infile.readline())
		for t in range(T):
			line = infile.readline()
			N = int(line.split()[0])
			J = int(line.split()[1])
			f.write("Case #1:\n")
			count = 0
			for i in range(2**(N-1)+1, 2**N, 2):
				x = str(bin(i)[2:])
				flag = 0
				arr = []
				for j in range(2,11):
					n = int(x,j)
					a,b = isprime(n)
					if a is True:
						flag = 1
						break
					else:
						arr.append(b)
				if flag == 1:
					continue
				else:
					f.write(x+" ")
					count += 1
					for n in arr:
						f.write(str(n)+" ")
					f.write("\n")
				if count == J:
					break
