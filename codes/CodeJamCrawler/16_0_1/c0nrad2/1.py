def calcLast(i):
  result = 10 * [0]

  if i == 0:
    return "INSOMNIA"

  delta = i
  while True:
    digits = getDigits(i)

    for digit in digits:
      result[digit] = 1

    if allDigits(result):
      return i
    i += delta

def allDigits(digits):
  for i in digits:
    if i == 0:
      return False
  return True

def getDigits(i):
  strInt = str(i)
  out = []
  for a in strInt:
    out.append(ord(a) - ord('0'))
  return out


fname = "1.txt"
with open(fname) as f:
  body = f.readlines()

t = int(body[0])

body = body[1:]

for i in range(t):
  print "Case #%d: %s" % (i+1, calcLast(int(body[i])))
