t = int (input())

for i in range(t):
	n=int(input())
	stri=input().split()
	a=65
	l=[]
	count=0
	for j in stri:
		l.append([chr(a),int(j)])
		a+=1
		count+=int(j)

	l=sorted(l,key=lambda l: l[1],reverse=True)
	ans=''
	while(1):
		if(l[0][1]==0):
			break

		if l[0][1]>=2:
			temp_c=count
			temp_c-=2
			if( temp_c>0 and (l[1][1]/temp_c>0.5)):
				count-=2
				l[0][1]-=1
				l[1][1]-=1
				ans+=l[0][0]+l[1][0]+' '

			else:
				count-=2
				l[0][1]-=2
				ans+=l[0][0]+l[0][0]+' '

		else:
			if( len(l)>2 and  l[2][1]==1):
				count-=1
				l[0][1]-=1
				ans+=l[0][0]+' '

			else:
				count-=2
				l[0][1]-=1
				l[1][1]-=1
				ans+=l[0][0]+l[1][0]+' '

		l=sorted(l,key=lambda l: l[1],reverse=True)


	
	z=i+1

	z=str(z)

	print('Case #'+z+': '+ans)








