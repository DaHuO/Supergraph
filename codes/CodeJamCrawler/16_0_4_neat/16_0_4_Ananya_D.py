import fileinput

case = -1
for line in fileinput.input():
  line = line.strip('\t\n\r')
  inputs = line.split(' ')
  K = int(inputs[0])
  case += 1
  if case == 0:
    continue
  l = range(1,K+1)
  l = map(lambda x: str(x), l)
  print "Case #%d: %s" % (case, " ".join(l))
