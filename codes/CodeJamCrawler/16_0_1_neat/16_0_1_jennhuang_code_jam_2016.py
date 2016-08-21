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

countingSheep()

      


