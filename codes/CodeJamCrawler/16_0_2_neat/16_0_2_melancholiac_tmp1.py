def pancakes(pans):
	times=0
	arr = list(pans)
	arr=map(lambda x:x=='+' and 1 or 0,pans)
	while len(filter(lambda x:x==0,arr))!=0:
		begin=arr[0]
		end=0
		if (not begin) in arr:
			end=arr.index(not begin)
		else:
			end=len(arr)
		arr[0:end]=map(lambda x : int(not x),arr[0:end])
		times+=1
	return str(times)
a=open('B-large.in','r').readlines()
attemps=int(a.pop(0))
attemps= 1<=attemps<=100 and attemps or 0
output=''
for i in range(attemps):
	if 0<=len(a[i][:-1])<=100:
		output+='Case #'+str(i+1)+': '+pancakes(a[i][:-1])+'\n'
with open('tempo_google.txt','w') as q:
	q.write(output)
