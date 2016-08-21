t=int(input())
for k in range(t):
	s=input()
	a={'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
	n=[]
	n.append(s[0])
	for i in range(1,len(s)):
		if a[n[0]] <= a[s[i]]:
			n.insert(0,s[i])
		else:
			n.append(s[i])
	m="Case #"+str(k+1)+":";
	print(m,''.join(n))

