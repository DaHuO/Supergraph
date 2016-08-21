t = int(raw_input())
for i in xrange(1, t + 1):
  a, b, c = [int(s) for s in raw_input().split(" ")] 
  answer = ''
  for j in xrange(1, a + 1):
    answer += ' ' + str(j)
  print "Case #{}:{}".format(i, answer)