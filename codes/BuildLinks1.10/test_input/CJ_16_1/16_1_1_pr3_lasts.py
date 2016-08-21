import sys
import math

## Promila Agarwal
## April 15, 2016
## The Last Word

def Pogo():
	
    in_f = open('lasts2.txt', 'r')
    out_f = open('last_out2.txt', 'w')
	
    num_of_case = int(in_f.readline().rstrip('\n'))
    for i in range(1, num_of_case+1):
        last(in_f, out_f, i)

 
def last(in_f, out_f, case_index): 
	instr = in_f.readline().rstrip('\n').split(" ")
	instr = list(''.join(instr))
	lin = len(instr)
	outs = list(instr[0])
	init = []
	current = 0
	for i in range(1,lin):
		if (instr[i] < outs[0]) :
			outs.append(instr[i])
			current +=1
			#print outs
		else :
			temp = list(instr[i])
			temp= temp + outs
			outs = []
			outs = temp
			current +=1
            #print outs
	
	#print outs
	str1 = ''.join(outs)
	#str1 = outs
	
	out_f.write("Case #{}: {}\n".format(case_index, str1))
	
def processC(in_f, out_f, case_index):
	in_str = in_f.readline().rstrip('\n').split(" ")
	in_str = ''.join(in_str)
	#print in_str
	lin = len(in_str)
	if (lin < 1):
		num_flips = 0
	else :
		flip_char = in_str[0]
		push_str = in_str[0]
		num_flips = 0
		for i in range(1,lin):
			if (flip_char == in_str[i]):
				#push_str.join(in_str[i])
				pass
			else :
				#pus_str, flip_char = flip(push_str,flip_char)
				if (flip_char == '-'):
					flip_char = '+'
				else :
					flip_char = '-'
				#push_str.join(in_str[i])
				num_flips +=1
        if (flip_char == '-'):
            #push_str, flip_char = flip(push_str,flip_char)
            num_flips +=1	
	str1 = str(num_flips)		
	out_f.write("Case #{}: {}\n".format(case_index, str1))
	
if __name__ == '__main__':    
    Pogo()
