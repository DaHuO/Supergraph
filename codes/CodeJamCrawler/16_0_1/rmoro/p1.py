###
## Robert Morouney
## moro1422@mylaurier.ca
## Friday April 08 2016
##
## Google_Code Jam Qualify_A: Couting Sheep
## 

def tbit(flg,bit):
	mask = 1 << bit
	return (flg & mask)

def sbit(flg,bit):
	mask = 1 << bit
	return (flg | mask)


def get_sleep_digit(N):
	d_flgs = 0b0000000000
	sleep_digit = N
	multiplier = 1
	no_op = 0
	while(d_flgs != 0b1111111111 ):
		sleep_digit = N * multiplier
		multiplier = multiplier + 1
		if multiplier > 50000: 
			break
		tmp_str = str(sleep_digit)
		for c in tmp_str:
			int_c = int(c)
			if tbit(d_flgs,int_c):
				no_op
			else:
				d_flgs = sbit(d_flgs,int_c)
	return sleep_digit if d_flgs == 0b1111111111 else 0
				
		

cases = 0
case = 0;
fout = open('A-large.out','w')
with open("A-large.in") as fin:
	for line in fin:

		if cases == 0:
			cases = int(line.strip())
		elif case > cases:
			break
		else:
			case = case + 1
			N = int(line.strip())
			sleep_digit = get_sleep_digit(N)
			fout.write("Case #{0}: {1}\n".format(case, sleep_digit if sleep_digit!=0 else "INSOMNIA"))
	fout.close()			
