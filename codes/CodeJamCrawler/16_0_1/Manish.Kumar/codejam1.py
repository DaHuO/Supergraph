h=open("try.in")
o=open("output.txt","a+")
f=h.readlines()
t =int(f[0])
for a in range(1,t+1):
	l=[]
	n = int(f[a])
	i=1
	while len(l) < 10 and i<100000 :
		x=n*i
		y=[int(char) for char in str(x)]
		l=list(set(l+y))
		i=i+1
	if i!=100000:
		o.write("Case #"+str(a)+": "+str(x)+"\n")
	else:
		o.write("Case #"+str(a)+": INSOMNIA\n")

