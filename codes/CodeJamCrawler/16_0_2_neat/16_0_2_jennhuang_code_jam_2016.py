from sets import Set
def countingSheep():
  f = open("input_small.txt", "r")
  text  = f.readlines()

  ntests = text[0]
  case = 1

  for i in xrange(1, len(text)):
    notSeen = Set()
    n = int(text[i].strip())
    cur = 0
    if n == 0:
      print "Case #" + str(i) + ":" + " INSOMNIA"
      continue 
    while len(notSeen) < 10:
      cur = str(int(cur)+n)
      for digit in cur:
        d = int(digit)
        notSeen.add(d)
    print "Case #" + str(i) + ":" + " " + str(cur)

#countingSheep()

def pancakes():
  f = open("input_small.txt", "r")
  text  = f.readlines()

  ntests = text[0]
  case = 1

  for i in xrange(1, len(text)):
    result = flips(text[i].strip())
    print "Case #" + str(i) + ":" + " " + str(result)        

def flips(pancakes):
  if len(pancakes) == 0:
    return 0

  i = len(pancakes)-1
  nFlips = 0
  while i >= 0:
    if pancakes[i] == "-":
      pancakes = reverse(pancakes[0:i+1])+pancakes[i+1:]
      nFlips += 1
    i -= 1
  return nFlips

def reverse(s):
  result = ""
  for c in s:
    if c == "+":
      result += "-"
    elif c == "-":
      result += "+"
  return result

pancakes()
