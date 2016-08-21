import random, math

def coin(fileData):

	inputData = open(fileData,'r')
	lines = inputData.readlines()
	N = int(lines[0])
	open('output.txt', 'w').close()
	outputData = open('output.txt', 'a')
	i = 0
	j = 1

	def anybaseto10(digits, base):

	    number = 0
	    digits = digits.rstrip()
	    for digit in digits:
	        number = base * number + int(digit)
	    return number

	def searchDivisor(number):

	    for i in range(2, int(math.sqrt(number) + 1)):
	        if number % i == 0:
	            return i
	    return 'none'
	            

	while j <= N:

		previous_coins = []
		i+=1
		raw = lines[i].split()
		length = int(raw[0])
		cases = int(raw[1])
		case_num = 1
		print('case #{0}:\n'.format(j))
		outputData.write('case #{0}:\n'.format(j))

		while case_num <= cases:
			divisors = []
			jamcoin = 'none'
			while (len(jamcoin) != length) or (jamcoin[0] != '1') or (jamcoin[-1] != '1'):
				jamcoin = str(bin(random.getrandbits(length+1))[2:])
				
			if (jamcoin not in previous_coins):

				previous_coins.append(jamcoin)
				cb2 = anybaseto10(jamcoin,2)
				cb3 = anybaseto10(jamcoin,3)
				cb4 = anybaseto10(jamcoin,4)
				cb5 = anybaseto10(jamcoin,5)
				cb6 = anybaseto10(jamcoin,6)
				cb7 = anybaseto10(jamcoin,7)
				cb8 = anybaseto10(jamcoin,8)
				cb9 = anybaseto10(jamcoin,9)
				cb10 = int(jamcoin)

				div2 = searchDivisor(cb2)
				if(div2 != 'none'):
					divisors.append(div2)
					div3 = searchDivisor(cb3)

					if(div3 != 'none'):
						divisors.append(div3)
						div4 = searchDivisor(cb4)

						if(div4 != 'none'):
							divisors.append(div4)
							div5 = searchDivisor(cb5)

							if(div5 != 'none'):
								divisors.append(div5)
								div6 = searchDivisor(cb6)

								if(div6 != 'none'):
									divisors.append(div6)
									div7 = searchDivisor(cb7)

									if(div7 != 'none'):
										divisors.append(div7)
										div8 = searchDivisor(cb8)

										if(div8 != 'none'):
											divisors.append(div8)
											div9 = searchDivisor(cb9)

											if(div9 != 'none'):
												divisors.append(div9)
												div10 = searchDivisor(cb10)

												if(div10 != 'none'):
													divisors.append(div10)


			if(len(divisors) == 9):
				str_div = ' '.join(str(divisor) for divisor in divisors)
				print('{0} {1}'.format(jamcoin,str_div))
				outputData.write('{0} {1}\n'.format(jamcoin,str_div))
				case_num += 1

	
		j +=1

coin('C-small-attempt0.in')