num_tests = int(raw_input())
for case_num in range(1, num_tests + 1):
  start = long(raw_input())
  num = start
  if not num:
    print 'Case #{0}: INSOMNIA'.format(case_num)
  else:
    seen = [False for i in range(10)]
    while not all(seen):
      for digit in str(num):
        seen[int(digit)] = True
      num += start
    print "Case #{0}: {1}".format(case_num, num - start)