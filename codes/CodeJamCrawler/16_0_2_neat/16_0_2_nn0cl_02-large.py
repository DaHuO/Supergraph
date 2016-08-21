#!/usr/bin/python
# -*- coding: utf-8 -*- 
import sys
from pprint import pprint
def rev(lv,ov,f,t):
	ll=lv;
	for x in range(f,t):
		ll[x]=ov
	return ll;
def reverseTo(lv):
	if(u"+" in lv):
		idx=lv.index(u"+");
	else:
		idx=len(lv);
	if(idx==0):
		idx2=lv.index(u"-");
		return rev(lv,u"-",0,idx2);
	return rev(lv,u"+",0,idx);

def solve(val):
	cnt=0;
	ret=list();
	l = list(str(val));
	ret = l;
	while(u"-" in ret):
		cnt=cnt+1;
		ret = reverseTo(l);
	return cnt;
if __name__ == "__main__":
	src = open('B-large.in','r')
	#src = open('A-large.in','r')
	out = open('out.txt','w')

	case = int(src.readline())
	for Tidx in range(0,int(case)):
		S = src.readline()
		result = solve(S)
		#pprint(result)
		output_src = 'Case #%(Tidx)d: %(result)s'%{'Tidx':Tidx+1,'result':result}
		out.write(output_src+'\n')
	src.close()
	out.close()
