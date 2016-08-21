def swap(s, i, j):
		while i < j :
			a = s[i]
			b = s[j]
			s = s[:i] +  ('+' if b == '-' else '-')  + s[i+1:]
			s = s[:j] + ('+' if a == '-' else '-') + s[j+1:]
			i,j = i + 1, j - 1
		if i == j:
			s = s[:i] + ('+' if s[i] == '-' else '-') + s[i+1:]
		return s

def find(s,l):
	bi = l - 1
	fi = 0
	count  = 0
	while(bi >= 0):
		while bi >= 0 and s[bi] != '-' : bi -= 1
		if bi >= 0:
			if s[0] == '-':
				s = swap(s,0,bi)
				count += 1
			else:
				fi = 0
				while fi < l and s[fi] != '-': fi += 1
				s = swap(s,0,fi - 1)
				count += 1
	return count

for i in range(1,int(input())+1):
	s  = input()
	print("Case #"+str(i)+":",find(s,len(s)))
