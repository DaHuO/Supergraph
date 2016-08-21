import itertools
print "Generating possible jamcoins"
possibles = ["".join(seq) for seq in itertools.islice(itertools.product("01", repeat=30), 5000000)] 
for i in range(0, len(possibles)):
  possibles[i] = "1" + possibles[i] + "1"
def base_convert(coin, base):
  res = 0
  num = list(reversed(coin))
  for i in range(0, len(num)):
    res += int(num[i]) * base ** i
  return res
def nontrivial_div(num): #num is type int
  div = 3
  while (num % div != 0):
    if(div > (num**0.25)):
      return -1
    div += 2
  return div
def isjamcoin(coin):
  print "Testing", coin
  if not(coin[0] == '1' and coin[len(coin)-1] == '1'):
    return False
  divs = []
  for i in range(2, 11):
    div = nontrivial_div(base_convert(coin, i))
    if div != -1:
      divs.append(div)
    else:
      return False
  if len(divs) < 9:
    return False
  return divs

counter = 0
jamcoins = []
print "Verifying jamcoins"
while len(jamcoins) < 500:
  p = isjamcoin(possibles[counter])
  if p:
    print "Coin Found!"
    print possibles[counter], p
    jamcoins.append((possibles[counter], p))
  counter += 1
print "Done!"
print "Writing to file..."
f = open('jamcoin.out', 'w')
f.write("Case #1:\n")

for coin in jamcoins:
    f.write(coin[0] + " " + str(coin[1]).replace(",","").replace("[","").replace("]", "")+"\n")
f.close()
print "Done!"



