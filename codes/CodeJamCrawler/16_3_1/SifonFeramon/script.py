import numpy
import string

if __name__ == "__main__":
	outputList = []
	with open("input.txt") as inputFile:
		lines = inputFile.readlines()
		outputList = []
		for i in range(1, int(lines[0])*2, 2):			
			N = lines[i]
			results = []
			if not(int(N) == 0):
				parties = string.ascii_letters[:int(N)]
				parties = parties.upper()
				mans = [int(t) for t in (lines[i+1]).split(' ')]
				while(sum(mans)> 0 and sum(mans) > len(parties)):
					max_conuters = max(mans)
					index_max = [i for i,j in enumerate(mans) if j == max_conuters ]
					if(len(index_max) > 1):
						if(max_conuters == 1 and len(parties) > 2):
							results.append(str(parties[index_max[0]]))
							mans[index_max[0]] -= 1
							continue
						else:
							results.append(str(parties[index_max[0]]) + str(parties[index_max[1]]))
							mans[index_max[0]] -= 1
							mans[index_max[1]] -= 1
							continue
					
					results.append(str(parties[index_max[0]]) + str(parties[index_max[0]]))
					mans[index_max[0]] -= 2
				
				if(len(parties)%2 == 0 and not(0 in mans)):
					for k in range(0, len(parties), 2):
						results.append(str(parties[k]) + str(parties[k+1]))
						
				else:
					if(len(parties)%2 != 0 and sum(mans)%2 != 0):
						for k in range(len(parties)):
							if (mans[k] != 0):
								results.append(str(parties[k]))
								mans[k] -= 1
								break

					pars = []
					for k in range(len(parties)):
						if (mans[k] != 0):
							pars.append(str(parties[k]))
						
						if(len(pars) == 2):
							results.append(str(pars[0]) + str(pars[1]))
							pars.clear()	
				
			outputList.append(results)
			
		with open("output.txt", "w") as fileOut:
			for k in range(len(outputList)):
				value_out = " ".join(outputList[k])
				
					
				line_write = "Case #" + str(k+1) + ": " + value_out + "\n"
				fileOut.write(line_write)