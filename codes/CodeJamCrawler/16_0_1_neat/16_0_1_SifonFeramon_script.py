import numpy

limit = 1000000000
infin = "INSOMNIA"

if __name__ == "__main__":
	outputList = []
	with open("input.txt") as inputFile:
		lines = inputFile.readlines()
		outputList = int(lines[0])*[-1]
		for i in range(1, int(lines[0])+1):			
			N = lines[i]
			if not(int(N) == 0):
				map_digits = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}
				for c in range(1,limit):
					number_current = int(N)*c
					for j in str(number_current):
						map_digits[j] = 1
					if sum(map_digits.values()) == 10:
						outputList[i-1] = number_current
						break
		
		with open("output.txt", "w") as fileOut:
			for k in range(len(outputList)):
				value_out = ""
				if (outputList[k] == -1):
					value_out = infin
				else:
					value_out = str(outputList[k])
					
				line_write = "Case #" + str(k+1) + ": " + value_out + "\n"
				fileOut.write(line_write)