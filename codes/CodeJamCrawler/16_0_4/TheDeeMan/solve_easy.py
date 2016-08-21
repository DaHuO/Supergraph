
def from_line_to_answer(inp):
  k, c, s = [int(i) for i in inp.split(' ')]

  if k > s:
    return "IMPOSSIBLE"
  answers = [str((n * k**(c-1) + 1)) for n in range(k)]
  answers_joined = ' '.join(answers)
  print answers_joined
  return answers_joined



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
    formatted_answer = output_formatted(line, case, from_line_to_answer)
    f_w.write(formatted_answer)
    f_w.write('\n')
    case += 1
  f_r.close()
  f_w.close()
  print "done!"



# test_read('test_data')
test_read('D-small-attempt0.in')


