import sys
import math
import time
## Promila Agarwal
## March 12, 2016
## Sheep Problem Large

def Pogo():
	
	in_f = open('sheep_sm_l.in', 'r')
	out_f = open('sheep1l.txt', 'w')
	num_of_case = int(in_f.readline().rstrip('\n'))
	for i in range(1, num_of_case+1):
		count_sheep(in_f, out_f, i)
	
def count_sheep(in_f, out_f, case_index):
	in_s = in_f.readline().rstrip('\n').split(" ")
	in_s = ''.join(in_s)
	in_s = int(in_s)
	#in_s = map(char, in_s)
	d = [False for x in range(10)]
	n = 1
	if (in_s == 0) :
		str1 = 'INSOMNIA'
	else :
		while (False in d):       
			p_s = str(n * in_s)
			l_in = len(p_s)
			for i in range(l_in):
				d[int(p_s[i])] = True
			n +=1		
		str1 = p_s

	out_f.write("Case #{}: {}\n".format(case_index, str1))
	return 
	
if __name__ == '__main__':    
    Pogo()
