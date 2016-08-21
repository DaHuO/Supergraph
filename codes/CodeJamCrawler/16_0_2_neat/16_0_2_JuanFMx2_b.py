'''
Created on Apr 8, 2016

@author: JuanFMx2
'''
import sys
import os.path
import traceback
import bisect

def revenge_of_the_pancakes(case_num,line_input):
  answer = 0
  try:
    moves = 0
    line_input = line_input.strip()
    prev_up = line_input[0] == "+"
    if not prev_up and line_input[0] != "-":
      raise Exception("Invalid Format!")
    for char in line_input:
      cur_up = char == "+"
      if not cur_up and char != "-":
        raise Exception("Invalid Format!")
      if prev_up and cur_up:
        pass
      elif prev_up and not cur_up:
        moves += 1
      elif not prev_up and cur_up:
        moves += 1
      elif not prev_up and not cur_up:
        pass
      prev_up = cur_up
    if not prev_up:
      moves += 1
    answer = moves
  except:
    traceback.print_exc()
    print "Error parsing line \n%s"%(line_input)
    sys.exit(0)
  print "Case #%s: %s"%(case_num,answer)

def parse_input(input_path, process_test_case_func):
  with open(input_path) as f:
    cur_line = f.readline()
    try:
      num_lines_to_process = int(cur_line)
    except:
      print "'%s' is not a number!" % cur_line
      sys.exit(0)
    
    for i in range(num_lines_to_process):
      line_1 = f.readline()
      process_test_case_func((i+1),line_1)
    content = f.readlines()

def main(input_path):
  if os.path.isfile(input_path):
    parse_input(input_path,revenge_of_the_pancakes)
  else:
    print "Unknown file: '%s'" % input_path
    sys.exit(0)
    
if __name__ == "__main__":
  if len(sys.argv) >= 2:
    main(sys.argv[1])
  else:
    print "Insufficient Parameters"
    sys.exit(0)