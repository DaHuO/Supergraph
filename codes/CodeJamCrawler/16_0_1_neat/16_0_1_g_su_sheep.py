T = 0;
N = 0;
i = 0;

T = int(input());
while(i < T):
	dig = set();
	N = int(input())
	if(N == 0):
		print("Case #"+str(i+1)+":\tINSOMNIA");
	
	else:
		n = 0
		while(len(dig) != 10):
			n = n + N;
			dig.update(set(map(int, str(n))));
		print("Case #"+str(i+1)+":\t"+str(n));
	i += 1