from copy import deepcopy as copy
from collections import Counter

""" 
This is obviously just a depth first search.

What you do is, write a method called string_contains. Also a method called remove_string
I'd say sort it,
and then you can regex. Then you write something called get_remaining_digits.
Given your string, if it's empty you return an empty list. You actually return
True, []

If it's not empty, you check string contains for each, then call remove_string for each,
and then try it out. If string_contains fails for each one, then that means you're at a
dud, and you return False, False. 



"""

def make_dict_for_string(string):
  d = {}
  for c in string:
    if c not in d:
      d[c]=0
    d[c]+=1
  return d

def dict_to_string(string_dict):
  final = ""
  for k in string_dict:
    final += (k*string_dict[k])
  return final

print dict_to_string(make_dict_for_string("stevena"))

def string_contains(sub_str, parent_str):
  sub_dict = make_dict_for_string(sub_str)
  parent_dict = make_dict_for_string(parent_str)
  for k in sub_dict:
    if k not in parent_dict:
      return False
    if sub_dict[k] > parent_dict[k]:
      return False
  return True

# print string_contains("asdff", "asdf")

def remove_stra_from_strb(str_a, str_b):
  if not string_contains(str_a, str_b):
    raise Exception("Check it first, you drangus!")
  d_a = make_dict_for_string(str_a)
  d_b = make_dict_for_string(str_b)
  for k in d_a:
    d_b[k]-=d_a[k]
  new_strb = dict_to_string(d_b)
  return new_strb

# print remove_stra_from_strb("alex", "aldebexa")

# NUMBER_STRINGS = ['ZERO','NINE','EIGHT',
#                   'SEVEN','SIX', 'FIVE',
#                   'FOUR', 'THREE', 'TWO', 'ONE']
# NUMBER_STRINGS = ['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']

NUMBER_STRINGS = ['ZERO','SIX','EIGHT','TWO', 'FOUR', 'SEVEN','FIVE', 'NINE', 'ONE', 'THREE']

NUMBERS = [0,6,8,2,4,7,5,9,1,3]


# NUMBERS = [0,9,8,7,6,5,4,3,2,1]
# NUMBERS = [0,1,2,3,4,5,6,7,8,9]

# STR_TO_NUM = dict(zip(ORDER_NUM_STR, ORDERED_NUMBERS))
STR_TO_NUM = dict(zip(NUMBER_STRINGS, NUMBERS))
print STR_TO_NUM


def figure_out_number_set(input_str):
  if input_str == "":
    return True, []
  
  for num in NUMBER_STRINGS:
    if string_contains(num, input_str):
      str_without = remove_stra_from_strb(num, input_str)
      worked, nums_of_remaining = figure_out_number_set(str_without)
      if worked:
        return True, [STR_TO_NUM[num]] + nums_of_remaining

  # didn't work
  return False, False


def figure_out_number_string(input_str):
  worked, num_list = figure_out_number_set(input_str)
  num_list = sorted(num_list)
  if not worked:
    return ""
  return "".join([str(i) for i in num_list])




print figure_out_number_string("NINEONEONE")
print figure_out_number_string('OZONETOWER')
print figure_out_number_string("WEIGHFOXTOURIST")
print figure_out_number_string("OURNEONFOE")
print figure_out_number_string("ETHER")


def output_formatted(inp, i, output_function):
  ans = output_function(inp)
  formatted = "Case #" + str(i) + ": " + str(ans)
  return formatted

def test_read(filename):
  write_filename = filename + "_answer"
  f_r = open(filename, 'r')
  first = True
  case = 1
  f_w = open(write_filename, 'w')
  for line in f_r.readlines():
    if first == True:
      first = False
      continue
    print "case: " + str(case)
    if not line:
      print "missing line?"
      continue
    line = line.strip()
    formatted_answer = output_formatted(line, case, figure_out_number_string)
    f_w.write(formatted_answer)
    f_w.write('\n')
    case += 1
  f_r.close()
  f_w.close()
  print "done!"

# test_read('test_data')
# test_read('A-small-attempt0.in')
# test_read('A-large.in')
# test_read('A-large.in')
test_read('A-large-two.in')


















