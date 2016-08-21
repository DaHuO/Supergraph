d = dict()
digits = "0123456789"

tests = input()
for test in range (tests):
  n = input()
  for c in digits:
    d[c] = 0
  for c in str(n):
    d[c] = 1
  if n == 0:
    res = "INSOMNIA"
  else:
    res = n
    while (1):
      for c in str(res):
        d[c] = 1
      b = True
      for c in digits:
        if d[c] == 0:
          b = False
      if b:
        break
      res += n
         
  print ("Case #" + str(test + 1) + ": " + str(res))
