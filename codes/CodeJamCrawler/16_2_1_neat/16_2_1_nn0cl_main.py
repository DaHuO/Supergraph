# -*- coding: utf-8 -*-
#!/usr/bin/env python


import sys

ndic={"ZERO":0,"ONE":1,"TWO":2, "THREE":3, "FOUR":4, "FIVE":5, "SIX":6,"SEVEN":7,"EIGHT":8,"NINE":9}
dic1 = {
'G': 'EIGHT', 
'X': 'SIX', 
'Z': 'ZERO', 
'U': 'FOUR', 
'W': 'TWO', 
}
dic2 = {
'H': 'THREE', 
'F': 'FIVE', 
#'R': 'THREE',
#'T': 'THREE', 
'O': 'ONE',
'S': 'SEVEN'
}
dic3={
#'V': 'SEVEN', 
'I': 'NINE'
}
dic4={
#'N': 'SEVEN', 
'E': 'FIVE'
}

dics = [dic1,dic2,dic3,dic4]

def solve(line):
	ret = []
	counter = {}
	for dic in dics:
		for c in line:
			if c in dic:#EIGHT
				if dic[c] in ndic:
					ret.append(ndic[dic[c]])
					for cc in dic[c]:
						line = line.replace(cc,"",1)
	ret.sort()
	return "".join(map(str,ret))
def main(IN, OUT):
	T = int(IN.readline())
	for index in range(T):
		OUT.write('Case #%d: %s\n' % (index + 1, solve(IN.readline())))

if __name__ == '__main__':
	file_in = sys.argv[1]
	file_out = sys.argv[2]
	f_in = open(file_in);
	f_out = open(file_out,'w');

	main(f_in, f_out)
	#print (dic)	
	f_in.close()
	f_out.close()
