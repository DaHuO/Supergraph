import numpy, itertools

if __name__ == "__main__":
	outputList = []
	with open("input.txt") as inputFile:
		lines = inputFile.readlines()
		for i in range(1, int(lines[0])+1):
			elementOutput = []
			list_arg = (len(lines[i]))*[0]
			list_arg = lines[i].split(" ")
			N, J = list_arg[0], list_arg[1]
			for number in itertools.product('01', repeat = int(N)):
				currentNumber = []
				if(number[0] == number[len(number)-1] == '1'):
					currentNumber.append("".join(number))
					for base in range(2,11):
						number_base = int("".join(number), base)
						d = 2
						flag_JamCoin = False
						while(d*d < number_base):
							if((number_base % d) == 0):
								currentNumber.append(d)
								flag_JamCoin = True
								break
							d += 1
							
						if(not(flag_JamCoin)):
							currentNumber[:] = []
							break
		
				if(len(currentNumber) != 0):
					elementOutput.append(currentNumber)
					
				
				if(len(elementOutput) == int(J)):
					outputList.append(elementOutput)
					break		
			
		with open("output.txt", "w") as fileOut:
			for k in range(len(outputList)):
				line_write = line_write = "Case #" + str(k+1) + ":" + "\n"
				fileOut.write(line_write)
				for e in range(len(outputList[k])):
					value_out = ""
					for g in range(len(outputList[k][e])):
						value_out += str(outputList[k][e][g])+" "
					
					fileOut.write(value_out)
					fileOut.write("\n")
			    