n=input()

def isValid(coin):
  dividers = []
  for base in xrange(2, 11):
    number = int(coin, base)
    #print base, number, coin
    divider = None
    for divisor in xrange(2, 10):
      if number % divisor == 0:
        prime = False
        divider = divisor
        break
    #print base, number, divider
    if divider == None:
      return None
    dividers.append(str(divider))
  return dividers

def jamCoins(n, j):
  t = 0
  for baseCoin in xrange(int('0'*(n-2), 2), int('1'*(n-2), 2) + 1):
    coin = '1' + ('{0:0'+str(n-2)+'b}').format(baseCoin) + '1'
    dividers = isValid(coin)
    if dividers != None:
      print coin, ' '.join(dividers)
      t += 1
    if t == j:
      break

for x in xrange(n):
  m, j = map(int, raw_input().split())
  print 'Case #'+str(x+1)+':'
  jamCoins(m, j)