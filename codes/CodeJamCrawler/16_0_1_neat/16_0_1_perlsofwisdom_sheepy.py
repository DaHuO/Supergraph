t = input()
for i in range(1,t+1) :
  N = input()
  print "Case #{}:".format(i),
  if N == 0 :
    print "INSOMNIA"
    continue
  Norig = N
  digits = [0]*10
  while True :
    #evaluate digits seen
    n = N
    while n != 0 :
      digits[n%10] = 1
      n /= 10
    if all(digits) :
      print N
      break
    N += Norig
    
