import sys, math

def coinJam(input):
  with open(input) as f:
    next(f)
    outfile = open('output.txt', 'w')
    T = 1
    for line in f:
      tokenizedLine = (line.rstrip()).split(' ')
      N = int(tokenizedLine[0])
      J = int(tokenizedLine[1])
      
      coinBody = '0' * (N-2)
      maxBody = int('1'*(N-2), 2)
      
      validCoins = []
      
      while len(validCoins) < J and int(coinBody, 2) <= maxBody:
        jamCoin = []
        coinId = '1%s1' % coinBody
        jamCoin.append(coinId)
        for base in range(2, 11):
          baseNum = int(coinId, base)
          isValid = False
          for divisor in range(2, int(math.ceil(math.sqrt(baseNum)))):
            if baseNum % divisor == 0:
              jamCoin.append(str(divisor))
              isValid = True
              break
          if not isValid:
            break
        if len(jamCoin) == 10:
          validCoins.append(jamCoin)
        coinBody = bin(int(coinBody, 2) + 1)[2:].zfill(N-2)
      
      outfile.write('Case #%d:\n' % T)
      for coin in validCoins:
        outfile.write(' '.join(coin) + '\n')
      T += 1
  
if __name__ == "__main__":
  if len(sys.argv) == 2:
    coinJam(sys.argv[1])
  else:
    print 'please specify an input file'