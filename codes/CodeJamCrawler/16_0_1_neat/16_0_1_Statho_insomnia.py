
inp = open('input.in', 'r')
outp = open('output.out', 'w')

t = int(inp.readline().rstrip())
count = 0
N = 0

for i in range(t):
	seen = [0,0,0,0,0,0,0,0,0,0]
   	n = inp.readline().rstrip()
	count += 1   	
	if(n == '0'): 
      		outp.write("Case #" + str(count) + ": INSOMNIA" +  "\n")
        else:
		l = int(n)
		N = l
		flag = 0
		while(flag == 0):
			m = map(int, str(N))
			for j in m:
				if(seen[int(j)] == 0):
					seen[int(j)] = 1

				if(sum(seen) == 10):
					outp.write("Case #" + str(count) +": " + str(N) + "\n")
					flag = 1 
					break;
        		N += l
			

outp.close()
inp.close()


