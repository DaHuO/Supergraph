import sys

def get_digits(filename):
  d = {'ZERO':0, 'ONE':1, 'TWO':2, 'THREE':3, 'FOUR':4, 'FIVE':5, 'SIX':6, 'SEVEN':7, 'EIGHT':8, 'NINE':9}
  num = {k:list(v) for v,k in d.iteritems()}
  # print num
  with open(filename, 'r') as f:
    T = int(f.readline().rstrip())
    for t in xrange(T):
      S = f.readline().rstrip()
      out = ''
      while 'Z' in S:
        for i in num[0]:
          S = S.replace(i, '', 1)
        out += str(d['ZERO'])
      while 'X' in S:
        for i in num[6]:
          S = S.replace(i, '', 1)
        out += str(d['SIX'])
      while 'W' in S:
        for i in num[2]:
          S = S.replace(i, '', 1)
        out += str(d['TWO'])
      while 'G' in S:
        for i in num[8]:
          S = S.replace(i, '', 1)
        out += str(d['EIGHT'])
      while 'U' in S:
        for i in num[4]:
          S = S.replace(i, '', 1)
        out += str(d['FOUR'])
      while 'S' in S:
        for i in num[7]:
          S = S.replace(i, '', 1)
        out += str(d['SEVEN'])
      while 'F' in S:
        for i in num[5]:
          S = S.replace(i, '', 1)
        out += str(d['FIVE'])
      while 'R' in S and 'H' in S:
        for i in num[3]:
          S = S.replace(i, '', 1)
        out += str(d['THREE'])
      while 'N' in S and 'I' in S:
        for i in num[9]:
          S = S.replace(i, '', 1)
        out += str(d['NINE'])
      while 'O' in S and 'N' in S:
        for i in num[1]:
          S = S.replace(i, '', 1)
        out += str(d['ONE'])

      print "Case #{}: {}".format(t+1, ''.join(sorted(out)))
if __name__ == '__main__':
  get_digits(sys.argv[1])