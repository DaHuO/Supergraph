def pancake(a):
	ans=0
	temp=a[0]
	if a=="":
		return 0
	for i in a:
		if i!=temp:
			ans+=1
			temp=i
	if i=="+":
		return ans
	else:
		return ans+1
t=input()
f=open("o.txt","w")
for i in range(1,t+1):
	f.write("Case #"+str(i)+": "+str(pancake(raw_input()))+"\n")
f.close()
