'''
Created on Apr 8, 2016

@author: JuanFMx2
'''
import sys
import os.path
import traceback
from fractions import gcd

known_primes = set()
asume_prime_after = 10000

def is_prime(n,asume_prime=False):
  if n in known_primes:
    return (True,-1)
  limit=n
  prime = True
  cur_div = 2
  while cur_div < limit:
    if n%cur_div == 0:
      prime = False
      break
    limit = n/cur_div
    cur_div += 1
    if asume_prime and cur_div > asume_prime_after:
      break
    while cur_div < limit and not is_prime(cur_div)[0]:
      cur_div += 1
  if prime:
    known_primes.add(n)
    return (prime,-1)
  else:
    return (prime,cur_div)

def calc_bases(str_num):
  coin_bases = []
  for base in range(2,11):
    coin_bases.append(int(str_num,base))
  return coin_bases

def coin_jam(case_num,line_input):
  answer = ""
  try:
    parts = line_input.split()
    n = int(parts[0])
    j = int(parts[1])
    found = 0
    cur_coin_id = int("0")
    
    while found < j:
      coin_id_bin = "1"+"{0:b}".format(cur_coin_id).zfill(n-2)+"1"
      if len(coin_id_bin) > n:
        break
      nums = calc_bases(coin_id_bin)
      has_prime = False
      trivial_divisors = []
      for num_i in nums:
        is_n_prime,td = is_prime(num_i,True)
        if is_n_prime:
          has_prime = True
          break
        else:
          trivial_divisors.append(td)
      if not has_prime:
        found+=1
        answer += coin_id_bin
        for td in trivial_divisors:
          answer += " %d"%td
        answer += "\n"

      cur_coin_id += 1
  except:
    traceback.print_exc()
    print "Error parsing line \n%s"%(line_input)
    sys.exit(0)
  print "Case #%s: \n%s"%(case_num,answer)

def parse_input(input_path, process_test_case_func):
  with open(input_path) as f:
    cur_line = f.readline()
    try:
      num_lines_to_process = int(cur_line)
    except:
      print "'%s' is not a number!" % cur_line
      sys.exit(0)
    
    for i in range(num_lines_to_process):
      cur_line = f.readline()
      if not cur_line:
        print "line %s is empty!" % cur_line
        sys.exit(0)
      process_test_case_func((i+1),cur_line)
    content = f.readlines()

def main(input_path):
  if os.path.isfile(input_path):
    parse_input(input_path,coin_jam)
  else:
    print "Unknown file: '%s'" % input_path
    sys.exit(0)
    
if __name__ == "__main__":
  if len(sys.argv) >= 2:
    main(sys.argv[1])
  else:
    print "Insufficient Parameters"
    sys.exit(0)