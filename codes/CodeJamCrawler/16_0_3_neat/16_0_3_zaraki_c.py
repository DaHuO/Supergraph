#!/usr/bin/python


mx_len = 6
ary = []

def gen(s):
	if len(s)==mx_len:
		ary.append('1'+s+'1');
		return
	gen(s+'1')
	gen(s+'0')



if __name__=='__main__':
	tst=int(input())

	for ks in range(1,tst+1):
		n,j=raw_input().split()
		j = int(j)
		s=''
		gen(s)
		print 'Case #%d:' %(ks)
		for i in range(j):
			print "%s %d %d %d %d %d %d %d %d %d" %(ary[i]+ary[i],
					int(ary[i],2),int(ary[i],3),int(ary[i],4),
					int(ary[i],5),int(ary[i],6),int(ary[i],7),
					int(ary[i],8),int(ary[i],9),int(ary[i],10))
	
