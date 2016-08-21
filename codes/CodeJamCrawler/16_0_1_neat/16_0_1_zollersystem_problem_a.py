import sys
import numpy as np

infile, outfile = sys.argv[1], sys.argv[2]

f = open(infile)

contents = np.array([int(line.strip()) for line in f])

f.close()
false = False
true = True
count = contents[0]

numbers = range(1, (int(count) + 1))
o = open(outfile, "a")

def generate_clean_num_array():
  return np.zeros(10)

def check_num_array_complete(num_array):
  for num in num_array:
    if num == 0:
      return False
  return True
case_number = 1
for i in contents[1:]:
  current_num_array = generate_clean_num_array()
  
  result_string = "Case #{0}: ".format(str(case_number))
  if i == 0:
    result_string = result_string + 'INSOMNIA'
  else:
    current_multiple = 1
    current_value = 0

    while not (check_num_array_complete(current_num_array)):
      current_value = i * current_multiple
      for digit in str(current_value):
        current_num_array[int(digit)] += 1
      current_multiple += 1
    result_string = result_string + str(current_value)
  o.write(result_string)
  case_number += 1
  o.write("\n")
o.close()