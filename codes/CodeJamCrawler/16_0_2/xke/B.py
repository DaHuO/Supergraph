import math

inputfile = open('B-large.in')
outputfile = open('B-large.out.txt', 'w')


def countUpside(listPancakes):
  count = 0
  for char in listPancakes:
    if char=='+':
      count = count + 1
  return count

def flipAll(listPancakes):
  for i in range(len(listPancakes)):
    if listPancakes[i]=='+':
      listPancakes[i] = '-'
    else:
      listPancakes[i] = '+'
  return listPancakes

def flipToLastDownside(listPancakes):

  startFlip = False
  for i in range(len(listPancakes)-1, -1, -1):  # from end to 1

    if startFlip==False and listPancakes[i]=='-':
      startFlip = True

    if startFlip==True:
      if listPancakes[i]=='+':
        listPancakes[i] = '-'
      else:
        listPancakes[i] = '+'

  return listPancakes

def oneFlipAndDone(listPancakes):
  # all down, and then up
  allDown = True
  for i in range(len(listPancakes)):
    if allDown==True and listPancakes[i]=='-':
      continue
    elif allDown==True and listPancakes[i]=='+':
      allDown = False
    elif allDown==False and listPancakes[i]=='+':
      continue
    elif allDown==False and listPancakes[i]=='-':
      return False # cannot do one flip and done 

  return True # CAN do one flip and done 


# function for parsing the data
def data_parser(pancakes):

    listPancakes = list(pancakes)

    numFlips = 0
    totalPancakes = len(pancakes)
    upsidePancakes = countUpside(listPancakes)

    while upsidePancakes != totalPancakes:

      #print "Flip " + str(numFlips) + ": " + str(listPancakes)

      if upsidePancakes == 0:
        listPancakes = flipAll(listPancakes)
        numFlips = numFlips + 1

      elif oneFlipAndDone(listPancakes):
        listPancakes = flipToLastDownside(listPancakes)
        numFlips = numFlips + 1

      else:
        listPancakes = flipToLastDownside(listPancakes)
        numFlips = numFlips + 1

      upsidePancakes = countUpside(listPancakes)
    
    return str(numFlips)


#skip first line
#next(inputfile)

#read first line:
num_cases = int(inputfile.readline())

for i in range(0, num_cases):
    pancakes = inputfile.readline().strip()
    output_line = "Case #" + str(i+1) + ": " + data_parser(pancakes)
    print output_line
    outputfile.writelines(output_line+"\n")

inputfile.close()
outputfile.close()
