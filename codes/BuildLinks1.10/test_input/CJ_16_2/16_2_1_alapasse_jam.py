def function(liste):
	res = ''
	res_liste = []
	a = 0 #0
	b = 0 #1
	k = 0 #2
	d = 0 #3
	e = 0 #4
	f = 0 #5
	g = 0 #6
	h = 0 #7
	i = 0 #8
	j = 0 #9
	for c in liste:
		if c == 'Z':
			a += 1
		elif c == 'U':
			e += 1
		elif c == 'X':
			g += 1
		elif c == 'G':
			i += 1
		elif c == 'F':
			f += 1
		elif c == 'W':
			k += 1
		elif c == 'V':
			h += 1
		elif c == 'H':
			d += 1
		elif c == 'I':
			j += 1
		elif c == 'N':
			b += 1
	res_liste = res_liste+[0]*a + [4]*e + [6]*g + [8]*i + [5]*(f-e) + [2]*k + [7]*(h-(f-e)) + [3]*(d-i) + [9]*(j-(f-e)-g-i) + [1]*(b-(h-(f-e))-2*(j-(f-e)-g-i))
	res_liste = sorted(res_liste)
	for c in res_liste:
		res = res+str(c)
	return res

print(function('OZONETOWER'))
print(function('WEIGHFOXTOURIST'))
print(function('OURNEONFOE'))
print(function('ETHER'))

def solution_jam():
	source = open("D:/Google/QualifJamCode16/A-large.in","r")
	output = open("D:/Google/QualifJamCode16/solution.txt","w")
	liste = source.readline()
	liste = liste.split('\n')
	for i in range(int(liste[0])):
		liste = source.readline()
		a = function(liste)
		output.write('Case #'+str(i+1)+': '+function(liste)+'\n')
	output.close()
	source.close()

solution_jam()