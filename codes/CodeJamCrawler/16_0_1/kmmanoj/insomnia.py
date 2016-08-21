def digitize(a):
	digits=[]
	while a!=0:
		digits.append(a%10)
		a=a//10
	return digits

t=int(raw_input())
for x in range(t):
	init=int(raw_input())
	set_digits=[]
	i=0
	while init!=0 and len(set_digits)!=10:
		num=init*i
		dig=digitize(num)
		for a in range(len(dig)):
			set_digits.append(dig[a])
		set_digits=list(set(set_digits))
		i+=1
	if init==0:
		output="INSOMNIA"
	else:
		output=str(init*(i-1))
	print "Case #"+str(x+1)+": "+output
