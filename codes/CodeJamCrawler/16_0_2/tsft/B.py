def num_flips(pancakes, desired):
  if len(pancakes) == 1:
    return 0 if pancakes == desired else 1
  else:
    bottom = pancakes[-1]
    return num_flips(pancakes[:-1], bottom) + (bottom != desired)

num_tests = int(raw_input())
for case_num in range(1, num_tests + 1):
  pancakes = raw_input()
  print "Case #{0}: {1}".format(case_num, num_flips(pancakes, '+'))

