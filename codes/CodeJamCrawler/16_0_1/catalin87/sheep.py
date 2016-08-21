import sys
import os;

os.remove('res.txt');
fx = open('res.txt', 'w');


def start_counting(i, c):
	c = str(c);
	f = open('res.txt', 'a');
	f.write("Case #");
	f.write(c);
	f.write(': ');
	
	counting = True;
	digits=[0,1,2,3,4,5,6,7,8,9];
	if counting:
		if int(i)==0:
			f.write('INSOMNIA\n');
		else:		
			x = 1;
			while counting == True:
			
				z = x*int(i);
				x = x+1;
				present = str(z);
				for digit in present:
					if counting:		
						if int(digit) in digits:
							digits.remove(int(digit));				
						if not digits:
							z = str(z);
							f.write(z);						
							f.write('\n');
							counting = False;
							#print digit,' FOUND! i=',i;
			


with open('A-large.in') as fi:
    lines = fi.readlines();

c = 0;
for number in lines:
	if c!=0:
		i = int(number);
		start_counting(i, c);
	c = c+1;
