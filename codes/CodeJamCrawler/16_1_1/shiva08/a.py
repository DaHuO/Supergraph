def fun(s):
	t="@"
	for a in s:
		if ord(a)>=ord(t[0]):
			t= a+t
		else:
			t=t+a
		p=a
	return t.replace('@',"")



f = open('A-large.in','r')
n = int(f.readline())
g = open("b.txt","w")
for i in range(n):
	c = f.readline().strip()
	d = fun(c)
	g.write("Case #"+str(i+1)+": " + str(d)+"\n")
g.close()
f.close()