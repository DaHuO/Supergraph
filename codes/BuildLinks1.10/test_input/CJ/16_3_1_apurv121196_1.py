for _ in range(int(input())):
	n=int(input())
	arr=[int(i) for i in input().split()]
	s=''
	if n==2:
		if arr[0]==arr[1]:
			for i in range(arr[0]):
				s+='AB '
			s=s.strip()
		else:
			if arr[1]>arr[0]:
				for i in range(arr[1]-arr[0]):
					s+='B '
				for i in range(arr[0]):
					s+='AB '
				s=s.strip()
			else:
				for i in range(arr[0]-arr[1]):
					s+='A '
				for i in range(arr[1]):
					s+='AB '
				s=s.strip()
		print('Case #{}: {}'.format(_+1,s))
		continue
	elif n==3:
		d={}
		s=''
		for i in range(len(arr)):
			d[chr(i+65)]=arr[i]
		l=sorted(d,key=d.__getitem__,reverse=True)
		i=0
		if d[l[1]]<d[l[0]]:
			a=d[l[1]]
			b=d[l[0]]
			#print('#{}#'.format(b-a))
			#d[l[i]]=d[l[i+1]]
			for k in range(b-a):
				s+=l[0]+' '
		if d[l[i+2]]<d[l[i+1]]:
			string=l[0]+l[1]
			for u in range(d[l[i+1]]-d[l[i+2]]):
				s+=string+' '
		f=l[0]
		r=l[1]+l[2]
		for o in range(d[l[i+2]]):
			s+=l[0]+' '
		for m in range(d[l[i+2]]):
			s+=r+' '
		print('Case #{}: {}'.format(_+1,s))
	else:
		d={}
		s=''
		for i in range(len(arr)):
			d[chr(i+65)]=arr[i]
		l=sorted(d,key=d.__getitem__,reverse=True)
		e=d[l[0]]
		index=0


		if d[l[0]]!=d[l[1]]:
			for i in range(d[l[0]]-d[l[1]]):
				s+=l[0]+' '
			d[l[0]]=d[l[1]]
		while index<len(l)-1 and d[l[index]]==d[l[index+1]]:
			index+=1
		if d[l[0]]==d[l[len(l)-1]]:
			index=len(l)-1
		for i in range(len(l)-1,index,-1):
			for j in range(d[l[i]]):
				s+=l[i]+' '
		if (index+1)%2!=0:
			for h in range(d[l[index]]):
				s+=l[index]+' '
			#print('doing this')
			index-=1
		o=0
		while o<=index:
			for u in range(d[l[o]]):
				s+=l[o]+l[o+1]+' '
			o+=2
		print('Case #{}: {}'.format(_+1,s))
		'''
		u=''
		for i in l:
			u+=i
		#while True:
			#for i in range(len(l)-1):
		i=0
		while i<len(l)-1:
			while d[l[i+1]]<d[l[i]]:
				s+=l[i]
				d[l[i]]-=1
			for j in range(d[l[i]]-1):
				s+=l[i]+l[i+1]+' '
			d[l[i]]=1
			d[l[i+1]]=1
			i+=2
		print(s)'''

