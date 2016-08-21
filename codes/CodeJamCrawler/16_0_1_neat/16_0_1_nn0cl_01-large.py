# -*- coding: utf-8 -*- 
import sys
from pprint import pprint

def solve(val):
	ret = str();
	if(int(val) == 0):
		return "INSOMNIA";
	i=int(0);
	s=set();
	while 1==1:
		i=i+1;
		v=int(val)*i;
		for x in list(str(v)):
			s.add(x);
		if(len(s) == 10):
			ret=v;
			break;
	return ret;
if __name__ == "__main__":
	src = open('A-large.in','r')
	out = open('out.txt','w')

	case = int(src.readline())
	for Tidx in range(0,int(case)):
		N = src.readline()
		result = solve(N)
		output_src = 'Case #%(Tidx)d: %(result)s'%{'Tidx':Tidx+1,'result':result}
		out.write(output_src+'\n')
		#print(output_src)
	src.close()
	out.close()
