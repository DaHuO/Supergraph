import math

inputfile = open('A-large.in')
outputfile = open('A-large.out.txt', 'w')


def seen_all_digits(listTracker):
  strTracker = "".join(listTracker)
  if strTracker=="1111111111":
    return True
  else:
    return False

# function for parsing the data
def data_parser(N):

    if N==0:
      return "INSOMNIA" # should be the only insomnia case!

    listTracker = list("0000000000") # 10-char string for each 0..9

    multiplier = 1

    baseN = N

    while seen_all_digits(listTracker)==False:
      N = baseN * multiplier

      strN = str(N)
      #print "Current N: "+strN

      for char in strN:
        intChar = int(char)
        listTracker[intChar] = '1'

      multiplier = multiplier + 1

    return str(N)


#skip first line
#next(inputfile)

#read first line:
num_cases = int(inputfile.readline())

for i in range(0, num_cases):
    N = int(inputfile.readline())
    output_line = "Case #" + str(i+1) + ": " + data_parser(N)
    print output_line
    outputfile.writelines(output_line+"\n")

inputfile.close()
outputfile.close()
