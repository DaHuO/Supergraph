import sys
infile = sys.argv[1]

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: 
    line.append(" 2")
    return False
  if n < 9: return True
  if n%3 == 0: 
    line.append(" 3")
    return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    #line.append(' \t',f)
    if n%f == 0:
      line.append(" %s" %f)
      return False
    if n%(f+2) == 0:
      line.append(" %s" % (f+2))
      return False
    f +=6
  return True    

def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
  return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

line = []
data = open(infile)
case = data.readline()
N,J =  map(int, data.readline().split())
sys.stdout.write("N,J = %s,%s\n" % (N, J))

i = '1'
for x in range(N-2):
  i += '0'
i += '1'

records = []
while len(records) < J:
  line = []
  if len(i) == N and i[-1] == '1':
    line.append('%s' % i)
    for b in range(2,11):
      totest = int(i, b)
      # line.append("testing %s in base %s (=%s)" % (i, b, totest))
      if is_prime(totest):
        line = []
        break
    else:
      records.append(i)
      print ' '.join(line)
  i = baseN( int(i, 2) +1, 2)
#line.append("WINNER: %s" % records)