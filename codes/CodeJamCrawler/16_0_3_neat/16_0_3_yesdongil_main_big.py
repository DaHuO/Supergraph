import os
import sys
import math
import itertools

def xrange(start, stop):
   i = start
   while i < stop:
       yield i
       i += 1

def is_prime(value) :
  ret = 0
  if (value % 2) == 0 :
    ret = 2
  elif (value % 3) == 0 :
    ret = 3
  else :
    limit = int(math.sqrt(value))
    index_limit = limit/6 + 1
    for i in xrange(1, index_limit) :
      prime_v = 6*i - 1
      if (value % prime_v) == 0 :
        ret = prime_v
        break

      prime_v = 6*i + 1  
      if (value % prime_v) == 0 :
        ret = prime_v
        break
      
      if(prime_v > 10000) :
        break
  return ret

def make_value(N, middle, base) :
  result = 1 + base**(N-1)
  mul = base
  while (middle > 0) :
    remainder = middle % 2
    if(remainder == 1) :
      result += mul
    mul=mul*base
    middle /= 2
  return result

def get_result(N, J) :
  ret = []
  result = []
  limit = 2**(N-2)
  prime_ret = 0
  list_count = 0
  for i in range(0, limit) :
    divisor_list = []
    for base in range(2, 11) :
      test_v = make_value(N, i, base)
      prime_ret = is_prime(test_v)
      if(prime_ret == 0) :
        break
      else :
        divisor_list.append(prime_ret)
    if(prime_ret > 0) :
      result.append(make_value(N, i, 10))
      result.extend(divisor_list)
      ret.append(result)
      result = []
      list_count += 1
    if(list_count == J) :
      break
  return ret
  
def Main():
  result_list = []
  arg = []
  CASE_N = int(raw_input())
  line = raw_input()
  arg = line.split()
  result_list = get_result(int(arg[0]), int(arg[1]))

  print 'Case #1:'
  for result in result_list :
    for result_one in result :
      sys.stdout.write(str(result_one) + ' ')
    sys.stdout.write('\n')

if __name__ == '__main__':
  sys.exit(Main())