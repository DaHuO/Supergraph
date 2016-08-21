import fileinput
import logging
from itertools import *

logging.basicConfig(level=logging.DEBUG)

import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]

def find_answer(lines):
  ''' Find the answer for this question '''
  num_lines = lines[0]
  a_str = ' '.join(lines[1:])
  a_list = a_str.split(' ')
  result_list = []
  a_list.sort()
  j = ''
  for i in a_list:
    if j == i:
      continue
    counts = a_list.count(i)
    if counts%2 != 0:
      result_list.append(i)
    j = i  
  
  result_list.sort(key=natural_keys)


  result = ' '.join(result_list)

   
 
  return result

def main():
  ''' Parse the input lines '''
  lines = [l.strip() for l in fileinput.input()]
  # Solve your problem here
  logging.debug(lines)
  n_tests = int(lines[0])
  start_test = 1
  for i in xrange(0, n_tests):
    n_lines = int(lines[start_test])*2
    tc = lines[start_test:start_test+n_lines]
    logging.debug(tc)
    n = find_answer(tc)
    print 'Case #{}: {}'.format(i+1, n)
    start_test += n_lines

if __name__ == '__main__':
  main()