
import numpy as np
import math
import warnings
import string
warnings.filterwarnings('ignore')



with open("A-small-attempt0.in", "r") as f:
		
		T = int(f.readline().strip())

		for i in range(T):
			print ("Case #" + str(i+1) + ": ",end="")
			

			T = f.readline().strip()
			l=[]
			i=-1
			while (T!='' and i<10):
				i+=1
				if ('Z' in T):
					l.append(0)
					T = T.replace("Z", "", 1)
					T = T.replace("E", "", 1)
					T = T.replace("R", "", 1)
					T = T.replace("O", "", 1)
				elif ('W' in T):
					l.append(2)
					T = T.replace("T", "", 1)
					T = T.replace("O", "", 1)
					T = T.replace("W", "", 1)
				elif ('U' in T):
					l.append(4)
					T = T.replace("F", "", 1)
					T = T.replace("O", "", 1)
					T = T.replace("U", "", 1)
					T = T.replace("R", "", 1)
				elif ('G' in T):
					l.append(8)
					T = T.replace("E", "", 1)
					T = T.replace("I", "", 1)
					T = T.replace("G", "", 1)
					T = T.replace("H", "", 1)
					T = T.replace("T", "", 1)
				elif ('X' in T):
					l.append(6)
					T = T.replace("S", "", 1)
					T = T.replace("I", "", 1)
					T = T.replace("X", "", 1)
				elif (('F' in T) and ('I' in T) and ('V' in T) and ('E' in T)):
					l.append(5)
					T = T.replace("F", "", 1)
					T = T.replace("I", "", 1)
					T = T.replace("V", "", 1)
					T = T.replace("E", "", 1)
				elif (('S' in T) and ('E' in T) and ('V' in T) and ('E' in T) and ('N' in T)):
					l.append(7)
					T = T.replace("S", "", 1)
					T = T.replace("E", "", 1)
					T = T.replace("V", "", 1)
					T = T.replace("E", "", 1)
					T = T.replace("N", "", 1)
				elif (('N' in T) and ('I' in T) and ('N' in T) and ('E' in T)):
					l.append(9)
					T = T.replace("N", "", 1)
					T = T.replace("I", "", 1)
					T = T.replace("N", "", 1)
					T = T.replace("E", "", 1)
				elif (('T' in T) and ('H' in T) and ('R' in T) and ('E' in T)):
					l.append(3)
					T = T.replace("T", "", 1)
					T = T.replace("H", "", 1)
					T = T.replace("R", "", 1)
					T = T.replace("E", "", 1)
					T = T.replace("E", "", 1)
				elif (('O' in T) and ('N' in T) and ('E' in T)):
					l.append(1)
					T = T.replace("N", "", 1)
					T = T.replace("O", "", 1)
					T = T.replace("E", "", 1)
			
			l = np.sort(l)
			out=""
			for i in range(len(l)):
				out += str(l[i])
			print (out)

			
			