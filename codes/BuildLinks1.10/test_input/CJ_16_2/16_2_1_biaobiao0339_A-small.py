import fileinput
import logging
import itertools
import re
logging.basicConfig(level=logging.DEBUG)

def remove_str(str1,str2):
  for i in str2:
      pos = str1.index(i)
      str1=str1[:pos] + str1[(pos+1):] 
  return str1    

def find_answer(lines):
  ''' Find the answer for this question '''
  numList = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
  num_dict = [{
    'Z': '0',
    'W': '2',
    'U': '4',
    'X': '6',
    'G': '8',
  },
  {
    'O':'1',
    'H':'3',
    'F':'5',
    'S':'7',
  },
  {
    'I': '9'
  }]
  numStr = lines[0]
  result = []

  while len(numStr)>0:
    for l in num_dict:
      for k,v in l.iteritems():
        count = numStr.count(k)
        if count>0:
          while count>0:
            numStr = remove_str(numStr, numList[int(v)])
            result.append(v)
            count -= 1
    # exist = True
    # temp = ''
    # for j in numList[case]:
      
    #   if not j in numStr:
    #     exist = False
    #     numStr += temp
    #     case +=1
    #     break
    #   temp += j
    #   pos = numStr.index(j)
    #   numStr=numStr[:pos] + numStr[(pos+1):] 
       
    # if exist:        
    #   result.append(str(case))
  # for x in xrange(3,6):
  #   group = itertools.combinations(numStr, x)
  #   for i in group:
  #     r_str = ''.join(i)
  #     if r_str in numList:
  #       print i
  #       result.append(str(numList.index(r_str)))
  result.sort()
  return ''.join(result)       
       

def main():
  ''' Parse the input lines '''
  lines = [l.strip() for l in fileinput.input()]
  # Solve your problem here
  logging.debug(lines)
  n_tests = int(lines[0])
  start_test = 1
  n_lines = 1
  for i in xrange(0, n_tests):
    tc = lines[start_test:start_test+n_lines]
    logging.debug(tc)
    n = find_answer(tc)
    print 'Case #{}: {}'.format(i+1, n)
    start_test += n_lines

if __name__ == '__main__':
  main()