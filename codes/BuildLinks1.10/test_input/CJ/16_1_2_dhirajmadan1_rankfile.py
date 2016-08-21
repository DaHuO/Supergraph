T=input();
ans=[];
for i in range(T):
	N=input();
	d=dict();
	for j in range(2*N-1):
		l=map(lambda x:int(x),raw_input().split());
		for k in l:
			if(d.has_key(k)):
				del d[k];
			else:
				d[k]=True;
	l=d.keys();
	l.sort();
	ans.append(l);

for i in range(T):
	print("Case #"+str(i+1)+":"),
	for j in ans[i]:
		print (str(j)),
	print('');		


