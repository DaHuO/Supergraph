import sys

def get_inputs():
  result = [ ]

  for line in sys.stdin:
    split = line.split()
    if (len(split) > 0):
      result.append(int(split[0]))

  return result

def get_curr_digits(num):
  return set(str(num))

def print_case(case_num, num):
  num_str = str(num)
  if num == 0:
    num_str = "INSOMNIA"
  print("Case #%d: %s" % (case_num, num_str))

def print_last_num(num):
  if num == 0:
    return 0
  else:
    mul = 1
    digits = set()
    max_size = 10
    # go until you see all digits
    while (len(digits) != max_size):
      curr_digits = get_curr_digits(mul * num)
      digits = digits.union(curr_digits)
      mul += 1
    # reduce offset
    mul -= 1
    return mul * num

def main():
  inputs = get_inputs()
  num_cases = inputs[0]
  # print outputs for each test case
  for case in range(1, num_cases + 1):
    num = inputs[case]
    val = print_last_num(num)
    print_case(case, val)

if (__name__ == "__main__"):
  main()

