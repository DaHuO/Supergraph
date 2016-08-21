import sys
for t in range(input()):
		a = list(raw_input().strip())
		s = a[0]
		for j in range(1,len(a)):
			if(a[j]>=s[0]):
				s = a[j]+s 
			else:
				s=s+a[j]
		print "Case ",
		sys.stdout.write("#"),
		print t+1,
		sys.stdout.write(":"),
		print "",s
