def flip(ch):
	if ch=='-':
		return '+'
	return '-'

f=open("input.txt")
t=int(f.readline())
f2 = open('out.txt', 'w')

for i in range(t):
	s=f.readline()
	s=list(s)
	count=0
	r=s[::-1]
	while (True):
		flag=0
		r=s[::-1]
		for j in range(0,len(r)):
			if r[j]=='-':
				flag=1
				if s[0]=='-':
					sije = len(r)-j
					for k in range(0,sije):
						s[k]=flip(r[j+k])
				else:
					for k in range(0,len(s)):
						if s[k]=='-':
							break
						s[k]='-'
				print("s=",s,"\n")
				count+=1
				break
		if flag==0:
			break
			
	f2.write("Case #"+str(i+1)+": "+str(count)+"\n")
f.close()
f2.close()

