fin = open('D-small-attempt0.in','r')
fout = open('small.out','w+')
		
def print_case(caseNum,tiles):
	fout.write('Case #%d:' % (caseNum+1))
	for tile in tiles:
		fout.write(' %d' % (tile))
	fout.write('\n')

totalCases = int(fin.readline())
for i in range(totalCases):
	line = fin.readline().split(' ')
	k=int(line[0])
	c=int(line[1])
	s=int(line[2])
	tiles = []
	for j in range(s):
		tiles.append(1+(k**(c-1))*j)
	print_case(i,tiles)
	
fout.close()
fin.close()