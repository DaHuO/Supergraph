import math

inputfile = open('D-small-attempt0.in')
outputfile = open('D-small-attempt0.out.txt', 'w')



# pick tile positions to know for sure whether there's at least 1 G tile in the artwork.

def tile_positions(K, C, S):


  # K = int number of tiles in the first / original sequence
  # C = int number of iterations / complexity after the first / original tile.
  # S = int number of grad students who can clean a tile; S=K in small data set

  # final artwork has K**C tiles

  # does this work for K==S?
  # should be quick and dirty solution...

  return ' '.join(map(str, range(1,S+1)))


  #numOriginalVariations = 2 ** K
  #variationInt = 0  # this will turn into a string
  #variationFormatter = "{0:0" + str(K)+"b}"




# --------------------------------------------


#skip first line
#next(inputfile)

#read first line:
num_cases = int(inputfile.readline())

for i in range(0, num_cases):
    
    line = inputfile.readline()

    # parse line: K C S
    numbers = line.split()
    K = int(numbers[0]) 
    C = int(numbers[1]) 
    S = int(numbers[2]) 

    output_line = "Case #" + str(i+1) + ": " + tile_positions(K, C, S)
    print output_line
    outputfile.writelines(output_line+"\n")

inputfile.close()
outputfile.close()
