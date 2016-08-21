def ouput_answer(inp):
  i = int(inp)
  if i is 0:
    return "INSOMNIA"
  unseen = set(range(10))
  j = 1
  while True:
    c = i * j
    str_c = str(c)
    l_c = list(str_c)
    for char in l_c:
      unseen.discard(int(char))
    if len(unseen) is 0:
      return c
    j += 1


def output_formatted(inp, i):
  ans = ouput_answer(inp)
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
    formatted_answer = output_formatted(line, case)
    f_w.write(formatted_answer)
    f_w.write('\n')
    case += 1
  f_r.close()
  f_w.close()
  print "done!"



# test_read('counting_sheep_test_data.txt')
# test_read('A-small-attempt0.in')
test_read('A-large.in')







# for i in range(100000):
#   ans =  ouput_answer(i)
#   if i % 99 == 0:
#     print ans

# count = 1
# for i in [0,1,2,11,1692]:
#   print output_formatted(i, count)
#   count += 1




