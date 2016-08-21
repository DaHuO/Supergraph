import sys
import math
import time
## Promila Agarwal
## April 30, 2016
## telephone numbers


def Pogo():
	
	in_f = open('Tell.in', 'r')
	out_f = open('GotTell.txt', 'w')
	num_of_case = int(in_f.readline().rstrip('\n'))
	for i in range(1, num_of_case+1):
		got_tel(in_f, out_f, i)
	   
def remove_str(original_s, remove_s) :
    for elm in remove_s:
        pos = original_s.index(elm)
        original_s = original_s[:pos]+original_s[pos+1:]
        
    return original_s
    
def unscramble(in_str):
    lin = len(in_str)
    linc = lin
    
    tel = ''
    while len(in_str) > 0 :
        if ('Z' in in_str):
            #in_str = remove_f(in_str,'ZERO')
            in_str = remove_str(in_str,'ZERO')
            #print in_str
            tel = tel + '0'
            
        elif ('W' in in_str):
            in_str = remove_str(in_str,'TWO')
            #print in_str
            tel = tel + '2'
            
        elif ('U' in in_str):
            in_str = remove_str(in_str,'FOUR')
            #print in_str
            tel = tel + '4'
            
        elif ('X' in in_str):
            in_str = remove_str(in_str,'SIX')
            #print in_str
            tel = tel + '6'
            
        elif ('G' in in_str):
            in_str = remove_str(in_str,'EIGHT')
            #print in_str
            tel = tel + '8'
            
        elif ('O' in in_str):
            in_str = remove_str(in_str,'ONE')
            #print in_str
            tel = tel + '1'
            
        elif ('H' in in_str):
            in_str = remove_str(in_str,'THREE')
            #print in_str
            tel = tel + '3'
            
        elif ('F' in in_str):
            in_str = remove_str(in_str,'FIVE')
            #print in_str
            tel = tel + '5'
            
        elif ('V' in in_str):
            in_str = remove_str(in_str,'SEVEN')
            #print in_str
            tel = tel + '7'
            
        elif ('I' in in_str):
            in_str = remove_str(in_str,'NINE')
            #print in_str
            tel = tel + '9'
            
                              
        
            
    return tel    

def got_tel(in_f, out_f, case_index):
	in_s = in_f.readline().rstrip('\n').split(" ")
	in_s = in_s[0]
	tel = unscramble(in_s)
	tel = list(tel)
	tel.sort()
	str1 = ''.join(tel)

	out_f.write("Case #{}: {}\n".format(case_index, str1))
	#out_f.write("Case #{}: \n{}".format(case_index, str1))
	return 
	
if __name__ == '__main__':    
    Pogo()
