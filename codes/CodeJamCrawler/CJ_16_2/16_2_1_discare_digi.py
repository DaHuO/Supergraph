#coding=utf-8

dataf = open('A-small-attempt0.in').readlines()
case = int(dataf[0].strip())
dataf = dataf[1:]

def getdigi(nl):
	#print nl,len(nl)
	if len(nl) == 0 :
		#print 'done'
		return []
	if 'Z' in nl :
		nl.remove('Z')
		nl.remove('E')
		nl.remove('R')
		nl.remove('O')
		cn = [0]
		cn.extend(getdigi(nl))
		return cn
	elif 'W' in nl : 
		nl.remove('T')
		nl.remove('W')
		nl.remove('O')
		cn = [2]
		cn.extend(getdigi(nl))
		return cn
	elif 'X' in nl :
		nl.remove('S')
		nl.remove('I')
		nl.remove('X')
		cn = [6]
		cn.extend(getdigi(nl))
		return cn
	elif 'G' in nl :
		nl.remove('E')
		nl.remove('I')
		nl.remove('G')
		nl.remove('H')
		nl.remove('T')
		cn = [8]
		cn.extend(getdigi(nl))
		return cn
	elif 'U' in nl :
		nl.remove('F')
		nl.remove('O')
		nl.remove('U')
		nl.remove('R')
		cn = [4]
		cn.extend(getdigi(nl))
		return cn
	elif 'R' in nl:
		nl.remove('T')
		nl.remove('H')
		nl.remove('R')
		nl.remove('E')
		nl.remove('E')
		cn = [3]
		cn.extend(getdigi(nl))
		return cn
	elif 'F' in nl and 'V' in nl :
		nl.remove('F')
		nl.remove('I')
		nl.remove('V')
		nl.remove('E')
		cn = [5]
		cn.extend(getdigi(nl))
		return cn
	elif 'V' in nl:
		nl.remove('S')
		nl.remove('E')
		nl.remove('V')
		nl.remove('E')
		nl.remove('N')
		cn = [7]
		cn.extend(getdigi(nl))
		return cn
	elif 'O' in nl :
		nl.remove('O')
		nl.remove('N')
		nl.remove('E')
		#print(type(nl))
		#ab = getdigi(nl)
		#print ab
		cn = [1]
		cn.extend(getdigi(nl))
		return cn
	else :
		nl.remove('N')
		nl.remove('I')
		nl.remove('N')
		nl.remove('E')
		cn = [9]
		cn.extend(getdigi(nl))
		return cn
		
	


for x in range(case):
	s = dataf[x].strip()
	#print(s)
	outn = getdigi(list(s))
	outn.sort(key = lambda y:y)
	print('Case #%d: %s' % (x+1,''.join([str(z) for z in outn])))
