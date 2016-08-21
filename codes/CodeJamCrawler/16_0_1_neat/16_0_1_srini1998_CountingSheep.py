t = int(raw_input())  # number of cases
#for i in xrange(1, t + 1):
#  n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
#  print "Case #{}: {} {}".format(i, n + m, n * m)
#  # check out .format's specification for more formatting options
master_digits = set([0,1,2,3,4,5,6,7,8,9]) 
for i in xrange(1, t + 1): 
  #number = [int(s) for s in raw_input()] # read a list of integers, 2 in this case
  orig_number = int(raw_input())
  num = orig_number
  #print "Case #{}: {} ".format(i, orig_number)
  # check out .format's specification for more formatting options
  j = 1
  while (len(master_digits) != 0):
    #print "number", n
    n = num
    if (n > 0):
      digits = set();
      while n:
        digit = n % 10
        #print "digit", digit
        digits.add(digit);
        n //= 10
      #print "digits ", digits
      master_digits = master_digits.difference(digits)
      #print "master_digits", master_digits
      if (len(master_digits) == 0):
        print "Case #"+str(i)+": "+str(num)
      else:
        j = j + 1
        num = orig_number * j
    else:
      print "Case #"+ str(i)+": INSOMNIA"
      master_digits = set()
  master_digits = set([0,1,2,3,4,5,6,7,8,9])