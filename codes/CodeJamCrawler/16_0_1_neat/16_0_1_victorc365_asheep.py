#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  asheep.py
#  
#  Copyright 2016 Victor  <victor@victor-Lenovo-G40-80>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  



def main():
	case = 0
	N=raw_input()
	try:
		while(case<=10000000):
			case =case + 1 
			N=raw_input()
			if N == '':
				return 0;
			N = int(N)
			digits = get_digits(N)
			i=1
			while(True):
				i=i+1
				N_new=N*i
				if N_new == N:
					print "Case #{}: INSOMNIA".format(case)
					break
				else:
					d = get_digits(N_new)
					for j in d:
						if not j in digits:
							digits.append(j)
					if verifica(digits):
						print "Case #{}: {}".format(case,N*i)
						break
	except(EOFError):
		return 0
	return 0
	
def get_digits(digit):
	# obtener los digitos del numero 
	str_digit=str(digit)
	list_digits = []
	for i in range(len(str_digit)):
		list_digits.append(int(str_digit[i]))
	return list_digits
	
def verifica(lista):
	# return true if the list is all digits, false other wise
	for n in range(10):
		if not n in lista:
			return False;
	return True;
		
if __name__ == '__main__':
	main()

