import fileinput
import logging
import re
import itertools
logging.basicConfig(level=logging.DEBUG)

def find_answer(lines):
  ''' Find the answer for this question '''
  alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  num = int(lines[0])
  arr = [int(i) for i in lines[1].split(' ')]
  total = sum(arr)
  results = []
  while total> 0:
    import operator
    index, value = max(enumerate(arr), key=operator.itemgetter(1))
    temp = alpha[index]
    arr[index] = value - 1
    total -= 1
    index, value = max(enumerate(arr), key=operator.itemgetter(1))
    if value*2 > total:
      temp += alpha[index]
      arr[index] = value - 1
      total -= 1
    index, value = max(enumerate(arr), key=operator.itemgetter(1))
    if value*2 > total:
      temp += alpha[index]
      arr[index] = value - 1
      total -= 1  
    results.append(temp)  
  
  result = ' '.join(results)
  return result

def main():
  ''' Parse the input lines '''
  lines = [l.strip() for l in fileinput.input()]
  # Solve your problem here
  logging.debug(lines)
  n_tests = int(lines[0])
  start_test = 1
  n_lines = 2
  for i in xrange(0, n_tests):
    tc = lines[start_test:start_test+n_lines]
    logging.debug(tc)
    n = find_answer(tc)
    print 'Case #{}: {}'.format(i+1, n)
    start_test += n_lines

if __name__ == '__main__':
  main()