import math

t = int(raw_input())
for i in xrange(1, t + 1):
  n, m = [int(s) for s in raw_input().split(" ")] 

  x = '1' + '0'*(n-2) + '1'
  i = 0
  answer = ''
  while i < m:
    x = '{:16b}'.format(2+int(x,2))
    jamcoin = str(x)
    coined = False
    for j in xrange(2, 11):
      coined = False
      y = int(x, j)
      if y % 2 == 0:
        coined = True
        jamcoin += ' 2'
      else:
        k = 3
        # what even are square roots
        while k < 15:
          if y % k == 0:
            coined = True
            jamcoin += ' ' + str(k)
            break
          k += 2
      if coined == False:
        break
    jamcoin += '\n'
    if coined == True:
      answer += jamcoin
      i += 1
  print "Case #{}:\n{}".format(t, answer)