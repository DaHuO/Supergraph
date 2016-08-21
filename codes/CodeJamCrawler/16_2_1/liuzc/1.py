import copy
t = int(input())  # read a line with a single integer

get =False
def dfs(dic,cnt,ans,level):
	
	global get
	if get:
		return 
	if level > 9:
		return
	if cnt == 0:
		print("Case #{}: {}".format(i,ans))
		get = True
	else:
			x = number[level]
			flag = True
			for l in x:
				if l not in dic or dic[l]<=0:
					flag= False
					break
			if flag:
				new_dic = copy.deepcopy(dic)
				for l in x:
					new_dic[l]=new_dic[l]-1
				dfs(new_dic,cnt-len(x),ans+str(level),level)
			dfs(dic,cnt,ans,level+1)
				
number = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

for i in range(1, t + 1):
	get=False
	n = (input().split()[0])  # read a list of integers, 2 in this case
	#a = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
	ans = ''
	dic={}
	for x in n:
		if x in dic:
			dic[x]=dic[x]+1
		else:
			dic[x]=1
	ans = dfs(dic,len(n),ans,0)
	# check out .format's specification for more formatting options
