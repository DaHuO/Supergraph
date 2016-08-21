"""
I might be able to solve it without solving it. I need a current state, and 
then I just iterate.

"""


def convert_elem(elem):
  if elem == '+':
    return True
  if elem == '-':
    return False
  print "SOMETHING BAD"
  raise Exception("bad elem: " + str(elem))

def convert_string(pancake_string):
  l = list(pancake_string)
  converted = [convert_elem(elem) for elem in l]
  return converted


def get_num_flips(pancake_string):
  converted = convert_string(pancake_string)
  reversed_converted = list(reversed(converted))
  current_state = True
  flips_needed = 0
  for pancake in reversed_converted:
    if pancake != current_state:
      flips_needed += 1
      current_state = (not current_state)

  return flips_needed
  # print reversed_converted

# this_str = "++++++"
# print convert_string(this_str)
# print get_num_flips(this_str)



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
    if not line:
      print "missing line?"
      continue
    line = line.strip()
    formatted_answer = output_formatted(line, case, get_num_flips)
    f_w.write(formatted_answer)
    f_w.write('\n')
    case += 1
  f_r.close()
  f_w.close()
  print "done!"


# test_read('test_data')
# test_read('B-small-attempt0.in')
test_read('B-large.in')

# print get_num_flips('-')
# print get_num_flips('-+')
# print get_num_flips('+-')
# print get_num_flips('+++')
# print get_num_flips('--+-')

# print convert_string("+---+--+--+")
# print convert_string("----")
# print convert_string("++++")





