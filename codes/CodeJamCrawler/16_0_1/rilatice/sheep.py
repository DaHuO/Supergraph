from sets import Set

def count_sheep(n):
	if n == 0: 
		return "INSOMNIA"
	remains = Set(['0','1','2','3','4','5','6','7','8','9'])
	i = 1
	while True:
		cur = i*n
		for j in str(cur):
			if j in remains:
				remains.remove(j)
		if len(remains) == 0:
			return str(cur)
		else:
			i += 1


inf = open("A-large.in","r")
outf = open("result.txt","w")
length = int(inf.readline())
for i in range(length):
	n = int(inf.readline().strip('\n'))
	result = count_sheep(n)
	outf.write('Case #%s: %s' %(i+1,result))
	if i < length -1:
		outf.write('\n')
inf.close()
outf.close()