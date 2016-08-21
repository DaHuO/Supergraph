t = int(raw_input())
def gen_next(arr,l):
	for i in range(1,l-1):
		if(arr[i]=='1'):
			arr[i]='0'
		else:
			arr[i]='1'
			break
	
def print_ans(arr,num,n):
	ans = [0 for i in range(11)]
	for i in range(2,11):
		num[i]=i
		ans[i]=1
		
	for i in range(1,n):
		if(arr[i]=='1'):
			for i in range(2,11):
				ans[i]+=num[i]
				num[i]=num[i]*i
		else:
			for i in range(2,11):
				num[i]=num[i]*i
	#arr.reverse()
	str1="".join(arr)
	str1=str1[::-1]
	#str1=reverse(str1)
	print(str1+str1),
	for i in range(2,11):
		print ans[i],
	print ""			
				
				
abc=0
for i in range(t):
	abc+=1
	print("Case #"+str(abc)+":")
	n,j = map(int,raw_input().split())
	n = n//2
	stri = ['0' for i in range(n)]
	stri[0]='1'
	stri[n-1]='1'
	
	count = 0
	num = [0 for i in range(11)]
	while(count<j):
		count+=1
		gen_next(stri,n)	
		
		print_ans(stri,num,n)

