n = int(input())

for i in range(1,n+1):
	number = []
	entrada = str(input())
	while 'Z' in entrada:
		entrada = entrada.replace('Z',"",1)
		entrada = entrada.replace('E',"",1)
		entrada = entrada.replace('R',"",1)
		entrada = entrada.replace('O',"",1)
		number.append("0")
	while 'W' in entrada:
		entrada = entrada.replace('W',"",1)
		entrada = entrada.replace('T',"",1)
		entrada = entrada.replace('O',"",1)
		number.append("2")
	while 'U' in entrada:
		entrada = entrada.replace('U',"",1)
		entrada = entrada.replace('F',"",1)
		entrada = entrada.replace('O',"",1)
		entrada = entrada.replace('R',"",1)
		number.append("4")
	while 'X' in entrada:
		entrada = entrada.replace('X',"",1)
		entrada = entrada.replace('I',"",1)
		entrada = entrada.replace('S',"",1)
		number.append('6')
	while 'G' in entrada:
		entrada = entrada.replace('G',"",1)
		entrada = entrada.replace('E',"",1)
		entrada = entrada.replace('I',"",1)
		entrada = entrada.replace('T',"",1)
		entrada = entrada.replace('H',"",1)
		number.append('8')
	while 'F' in entrada:
		entrada = entrada.replace('F',"",1)
		entrada = entrada.replace('I',"",1)
		entrada = entrada.replace('V',"",1)
		entrada = entrada.replace('E',"",1)
		number.append('5')
	while 'T' in entrada:
		entrada = entrada.replace('T',"",1)
		entrada = entrada.replace('H',"",1)
		entrada = entrada.replace('R',"",1)
		entrada = entrada.replace('E',"",2)
		number.append('3')
	while 'O' in entrada:
		entrada = entrada.replace('O',"",1)
		entrada = entrada.replace('N',"",1)
		entrada = entrada.replace('E',"",1)
		number.append('1')
	while 'I' in entrada:
		entrada = entrada.replace('I',"",1)
		entrada = entrada.replace('N',"",2)
		entrada = entrada.replace('E',"",1)
		number.append('9')
	while 'S' in entrada:
		entrada = entrada.replace('S',"",1)
		entrada = entrada.replace('E',"",2)
		entrada = entrada.replace('V',"",1)	
		entrada = entrada.replace('N',"",1)
		number.append('7')
	print("Case #" + str(i) + ": " + "".join(sorted(number)))