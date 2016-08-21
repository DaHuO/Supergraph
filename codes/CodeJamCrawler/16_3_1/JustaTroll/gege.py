t = int(input()) 

def fufu(n,l):
	#print (l)
	a = ''
	flag =1
	while (flag):
		if n>3:
			ma = max(l)
			c = []
			for i in range(0,len(l)):
				if l[i]==ma:
					c.append(i)
			if len(c)>1:
				a = a + chr(65+c[0]) + chr(65+c[1]) + " "
				l[c[0]]=l[c[0]]-1
				l[c[1]]=l[c[1]]-1
			else:
				a = a + chr(65+c[0]) + chr(65+c[0]) + " "
				l[c[0]]=l[c[0]]-2
			n = n -2
		elif n==3:
			ma = max(l)
			for i in range(len(l)):
				if l[i]==ma:
					c = i
			a = a + chr(65+c) + " "
			l[c] = l[c]-1
			n = n - 1
		else:
			ma = max(l)
			flag = 0
			c = []
			for i in range(0,len(l)):
				if l[i]==ma:
					c.append(i)
			a = a + chr(65+c[0]) + chr(65+c[1])
			n = n-2
	return a




for i in range(1, t+1):
  s = int (input())
  l = list(input().split(" "))
  for j in range(len(l)):
  	l[j]=int(l[j])
  p = sum(l)

  #print (s)
  #print ("ujnsdfjklsf", i)
  print ("Case #{}: {} ".format(i, fufu(p,l)))