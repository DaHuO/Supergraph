


ntests = int(input())



for i in range(ntests):
  digits = {}
  n = int(input())
  if n == 0:
    print("Case #{0}: {1}".format(i+1, "INSOMNIA"))
    continue
  k = 1
  while (True):
    num = str(n * k)
    k += 1
    for dig in num:
      digits[dig] = 1
    if len(digits.keys()) == 10:
      print("Case #{0}: {1}".format(i+1, num))
      break
