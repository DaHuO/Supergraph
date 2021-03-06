'''
Created on Apr 8, 2016

@author: JuanFMx2
'''
import sys
import os.path
import traceback
import math

def counting_sheep(case_num,line_input):
  answer = "INSOMNIA"
  try:
    num_n = long(line_input)
    if num_n != 0:
      digits_check = set()
      i = 0L
      while len(digits_check) < 10:
        i += 1
        cur_n = num_n*i
        if cur_n < 0:
          cur_n = -cur_n
        while cur_n>0:
          digits_check.add(cur_n%10)
          if len(digits_check) == 10:
            break
            break
          cur_n/=10
      answer = i*num_n
  except:
    traceback.print_exc()
    print "Error parsing line '%s'"%line_input
    sys.exit()
  print "Case #%s: %s"%(case_num,answer)

def parse_input(input_path, process_line_func):
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
      process_line_func((i+1),cur_line)
    content = f.readlines()
    

def main(input_path):
  if os.path.isfile(input_path):
    parse_input(input_path, counting_sheep)
  else:
    print "Unknown file: '%s'" % input_path
    sys.exit(0)
    
if __name__ == "__main__":
  if len(sys.argv) >= 2:
    main(sys.argv[1])
  else:
    print "Insufficient Parameters"
    sys.exit(0)