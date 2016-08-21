import sys

filename=sys.argv[1]

def count(start):
	if int(start)==0:
		return 'INSOMNIA'
	dic={}
	number = start
	i=1
	#prev_s=0
	while True:
		#print number,
		for digit in number:
			dic[digit]=1
		s = sum( dic.values() )
		if s==10:
			return number
		#if prev_s==s:
		#	return 'INSOMNIA'
		i+=1
		number = str( int(start)*i ) 
		prev_s = s

	return 'INSOMNIA'

f = open(filename,'rt')
cnt = f.readline()
i=0
for l in f.readlines():
	i+=1
	start = l.strip()
	res = count(start)
	print 'Case #'+str(i)+':',res 
