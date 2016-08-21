def fractile(k,c,s):
	ans=""
	for i in range(1,k+1):
		ans+=str(i)+" "
	return ans
t=input()
f=open("o.txt", "w")
for i in range(1,t+1):
	k,c,s=map(int, raw_input().split())
	f.write("Case #"+str(i)+": "+ fractile(k,c,s)+"\n")
f.close()
