from sys import stdin, stdout
t = int(stdin.readline())
for i in range(1, t+1):
	 n = int(stdin.readline())
	 stdout.write("Case #"+str(i)+": ")
	 if n == 0:
	 	stdout.write("INSOMNIA")
	 else:
	 	s = set()
	 	j = 0
	 	while len(s) < 10:
	 		j += n
	 		for k  in str(j):
	 			s.add(k)
	 	stdout.write(str(j))
	 stdout.write('\n')