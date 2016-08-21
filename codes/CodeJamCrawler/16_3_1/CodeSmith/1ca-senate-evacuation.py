# Round1A : Rank and File
import copy

def run():
	i = 0
	alps =  'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	with open('input.txt', 'rt') as src, open('output.txt', 'wt') as tgt:
		cases = int(src.readline())
		i = 1
		while(i <= cases):
			
			line = src.readline().rstrip('\r\n')
			N = int(line)
			ps = src.readline().rstrip('\r\n').split(' ')
			parties = list()
			
			for j in range(0, N):
				parties.append(alps[j] * int(ps[j]))
				
			cp = copy.deepcopy(parties)
			output = ''
			while True:
				for k in range(0, N):
					pair = ''
					cp = sorted(copy.deepcopy(parties), key=len, reverse=True)
					if(len(cp[k]) > 0):
						pair = cp[k][-1:]
						cp[k] = cp[k][:-1]
						
						
					for m in range(0, N+1):
						if(m < N and len(cp[m]) > 0):
							pair = pair + cp[m][-1:]
							cp[m] = cp[m][:-1]
						
						cp = sorted(cp, key=len, reverse=True)
						if len(cp[0]) == len(cp[1]):
							parties = cp
							if output == '':
								output = pair
							else:
								output =  output + ' ' + pair
							break
							
					if len(cp[0]) == len(cp[1]):
						break
				
				if len(cp[0]) == 0:
					break
					
			print 'Case #%s: %s' % (i, output)
			tgt.write("Case #%d: %s\n" % (i, (output)))
			i=i+1
				
run()