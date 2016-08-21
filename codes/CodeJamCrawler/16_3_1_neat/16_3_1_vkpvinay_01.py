# your code goes here
def smax(numbers):
    count = 0
    m1 = m2 = float('-inf')
    for x in numbers:
        count += 1
        if x > m2:
            if x >= m1:
                m1, m2 = x, m1            
            else:
                m2 = x
    return m2 if count >= 2 else None 
    
    
for i in range(1,int(input())+1):
	n=int(input())
	l=input().split()
	p=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	d=dict()
	for j in range(n):
		d[p[j]]=int(l[j])
	ans=[]
	s=sum(d.values())
	while(s>0):
		l=d.values()
		s=sum(l)
		m=max(l)
		sm=smax(l)
		tmp=''
		tmp1='    '
		if (((s-2)//2)>=(m-1)) and (((s-2)//2)>=(sm-1)):
			if m!=sm:
				tmp=list(d.keys())[list(d.values()).index(m)][0]
				tmp1=list(d.keys())[list(d.values()).index(sm)][0]
			else:
				tk=list((key for key,value in d.items() if value==m))
				tmp,tmp1=tk[0],tk[1]
			d[tmp]-=1
			d[tmp1]-=1
			ans.append(tmp+tmp1)
		elif (s-2)//2>=m-2 and m>=2:
			tmp=list(d.keys())[list(d.values()).index(m)][0]
			#if m>=2:
			d[tmp]-=2
			ans.append(tmp+tmp)
			# else:
			# 	d[tmp]-=1
			# 	ans.append(tmp)
		else:
			tmp=list(d.keys())[list(d.values()).index(m)][0]
			d[tmp]-=1
			ans.append(tmp)
	tmp=ans.pop()
	lst=ans.pop()
	if len(lst)==1:
		slst=ans.pop()
		ans.append(lst)
		ans.append(slst)
	else:
		ans.append(lst)
	print('Case #{}: {}'.format(i,' '.join(ans)))