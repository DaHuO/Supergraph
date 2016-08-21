t=int(raw_input())
for i in range(t):
	s=raw_input().strip()
	str_list=list(s)
	ans=[]
	for j in range(len(str_list)):
		if j==0:
			ans.append(str_list[j])
		else:
			if ans[0] <= str_list[j]:
				ans.insert(0,str_list[j])
			else:
				ans.append(str_list[j])
	print 'Case #' + str(i+1) + ': ' + ''.join(ans)
		
