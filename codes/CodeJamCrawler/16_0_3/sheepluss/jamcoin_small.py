import math

def jamcoin_small(ncase, length, ncoins):
  curcount = 0
  decimal = 1
  coins = {}
  while curcount < ncoins:
    curcoin = "1"
    binary = "1"
    j = decimal
    #print j
    while j>0:
      if j%2==0:
        binary = "0" + binary
      else:
        binary = "1" + binary
      j /= 2
    #print "Binary :%s" % binary
    while len(curcoin) < length - len(binary):
      curcoin += "0"
    #print "Base coin: %s" % curcoin
    curcoin += binary
    divisors = [-1 for i in xrange(2,11)]
    #print "Coin: %s" % curcoin
    for base in xrange(2,11):
      #print "Base: %d" % base
      val = 1 + base ** (length-1)
      for i in xrange(1, length-1):
        if curcoin[length-i-1]=="1":
          val += base ** i
      #print "Value: %d" % val
      if val%2==0:
        divisors[base-2] = 2
        continue
      if val%3==0:
        divisors[base-2] = 3
        continue
      val_sqrt = math.floor(math.sqrt(val))
      divisor_anchor = 6
      divisor = None
      while divisor is None and divisor_anchor <= val_sqrt+1:
        #print "Anchor: %d" % divisor_anchor
        if val%(divisor_anchor-1)==0:
          divisor = divisor_anchor-1
        elif val%(divisor_anchor+1)==0:
          divisor = divisor_anchor+1
        divisor_anchor += 6
      if divisor is None:
        break
      else:
        divisors[base-2] = divisor
    if -1 not in divisors:
      #print "Not prime"
      coins[curcoin] = divisors
      curcount += 1
    #else:
      #print "Prime"
    #print coins
    #print curcount
    decimal += 1
  return coins


ncases = int(raw_input().strip())
for i in xrange(1, ncases+1):
  params = raw_input().strip().split(" ")
  coins = jamcoin_small(i, int(params[0]), int(params[1]))
  print "Case #%d:" % i
  for key, val in coins.iteritems():
    print key,
    for v in val:
      print v,
    print
