import math
import sys



debugMode = False

if (len(sys.argv) <= 1):
  print('Please give input filename as argument')
  exit(-1)

my_file = sys.argv[1]

def debugPrint(msg):
  if (debugMode == True):
    print(msg)
  


f = open(my_file,'r')
counter = 0
cases = []
casesNumber = 0 


def getCases():
  cases = f.readline()
  debugPrint('Cases: ' + cases)
  for i in range(int(cases)):
    print('Case #' + str(i + 1) + ': ' + getGroups(i))
 
def getResults(results):
  kResults = True
  debugPrint(results)
  for res in results:
    kResults = kResults and res
  return kResults
  
def getGroups(i):  
  case = f.readline().strip('\n')
  numCase = int(case)
  initialCase = case
  debugPrint('----------------------------')
  results = [False for i in range(10)]
  k = 1
  previous = 0
  while ((getResults(results) == False)):   
    debugPrint('Initial: ' + initialCase)
    debugPrint('Case: ' + str(numCase) + ' K: ' + str(k))   
    if (previous == numCase):
      return 'INSOMNIA'
    numCase = k * int(initialCase)
    case = str(numCase)
    debugPrint(case)
    debugPrint(str(k))
    j = 0
    while (j < len(str(case))):
      debugPrint('Letter ' + case[j])
      results[int(case[j])] = True
      j = j + 1
    k = k + 1    
  return case
  
    
    
  


 
  
getCases()
