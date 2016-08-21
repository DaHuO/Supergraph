#!/usr/bin/python3.4


with open("input.in","r") as file:
	with open("output.out","w") as out:
		i = 0
		for line in file:
			if i != 0:	
				digits = []
				n = int(line)	
				rep = "INSOMNIA"
				if n != 0:
					for k in range(1,20000):
						a = str(k*n)
						for c in a:
							b = False
							for j in range(0,len(digits)):
								if digits[j] == c:
									b = True
							if b == False:
								digits.append(c)
						if len(digits) == 10:
							rep = a
							break
							
				sent = "Case #"+str(i)+": "+rep+"\n"
				print(sent)
				out.write(sent)
				
			i+=1
