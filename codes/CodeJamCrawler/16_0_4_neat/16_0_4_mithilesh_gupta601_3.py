f=open("input.txt")
t=int(f.readline())
f2 = open('out2.txt', 'w')


for i in range(t):
	s=f.readline()
	s=s.split(" ")
	k,c,s=int(s[0]),int(s[1]),int(s[2])
	if k==1:
		ans="1"
		f2.write("Case #"+str(i+1)+": "+ans+"\n")
		continue
	val = k**c
	arr=[]
	arr.append("1")
	diff=(val-1)//(k-1)
	for j in range(2,k):
		arr.append(str(1+(diff*(j-1))))
	arr.append(str(val))
	ans=' '.join(arr)
	f2.write("Case #"+str(i+1)+": "+ans+"\n")
f.close()
f2.close()

