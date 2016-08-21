t = int(raw_input())
for case in xrange(1, t+1):
  numbers = {str(x) for x in range(10)}
  cad = raw_input()
  tam = len(cad)
  num = int(cad)
  last_num = None
  factor = 1
  if num == 0:
    last_num = "INSOMNIA"
  else:
    while(numbers):
      last_num = factor * num
      numbers = numbers - set(str(last_num))
      factor += 1
  print "Case #{}: {}".format(case, last_num)