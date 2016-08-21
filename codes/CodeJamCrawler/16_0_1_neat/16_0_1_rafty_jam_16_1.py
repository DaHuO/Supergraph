import sys
t=input()
i=1
while i<=t:
	n=input()
	if n==0:
		print "{}{}{}".format("Case #",i,": INSOMNIA")
		i=i+1
		continue
	q=1
	arr=[0,0,0,0,0,0,0,0,0,0]
	while 1:
		k=n*q
		r=k
		while r>0:
			s=r%10
			arr[s]=1
			r=r/10
		if arr[0]+arr[1]+arr[2]+arr[3]+arr[4]+arr[5]+arr[6]+arr[7]+arr[8]+arr[9]==10:
			print "{}{}{}{}".format("Case #",i,": ",k)
			break
		q=q+1
	i=i+1
