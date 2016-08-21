import numpy

if __name__ == "__main__":
	outputList = []
	with open("input.txt") as inputFile:
		lines = inputFile.readlines()
		outputList = int(lines[0])*[-1]
		for i in range(1, int(lines[0])+1):
			pancakes_list = (len(lines[i]))*[0]
			for p in range(len(lines[i])):
				if(lines[i][p] == '-'):
					pancakes_list[p] = 0
				else:
					pancakes_list[p] = 1

			countFlip = 0
			if(len(pancakes_list) == 1):
				if(pancakes_list[0] == 0):
					outputList[i-1] = 1
				else:
					outputList[i-1] = 0
			else:
				while(sum(pancakes_list) != len(pancakes_list)):
					counter_pancakes = 1;
					while((counter_pancakes < len(pancakes_list)) and (pancakes_list[counter_pancakes-1] == pancakes_list[counter_pancakes])):
						counter_pancakes += 1

					for s in range(counter_pancakes):
						pancakes_list[s] = int(not(pancakes_list[s]))
									
					countFlip += 1
			
				outputList[i-1] = countFlip
			
		with open("output.txt", "w") as fileOut:
			for k in range(len(outputList)):
				value_out = str(outputList[k])
					
				line_write = "Case #" + str(k+1) + ": " + value_out + "\n"
				fileOut.write(line_write)