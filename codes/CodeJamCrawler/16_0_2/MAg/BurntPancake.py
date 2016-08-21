## Maneesh Agarwal
## April 9, 2016
## burnt pancake of same size 

def Call_Me():
	
    ib_f = open('ib_pancake.txt', 'r')
    ob_f = open('ob_pancake.txt', 'w')
	
    T = int(ib_f.readline().rstrip('\n'))
    for i in range(1, T+1):
        Num_of_Flips(ib_f, ob_f, i)

def Flip(t_char):
    if (t_char == '-'):
        t_char = '+'
    else :
        t_char = '-'
    return t_char
        
def Num_of_Flips(ib_f, ob_f, c_index):
	in_str = ib_f.readline().rstrip('\n').split(" ")
	in_str = ''.join(in_str)
	l_in = len(in_str)
	if (l_in < 1):
		num_flips = 0
	else :
		flip_char = in_str[0]
		
		num_flips = 0
		for i in range(1,l_in):
			if (flip_char <> in_str[i]):
							
				num_flips +=1
                		flip_char = Flip(flip_char)
                
        if (flip_char == '-'): # to account for last -
            num_flips +=1	
	str_flips = str(num_flips)		
	ob_f.write("Case #{}: {}\n".format(c_index, str_flips))
	
if __name__ == '__main__':    
    Call_Me()
