import sys

def count_sheep(filename):
  with open(filename) as f:
    T = int(f.readline())
    for t in range(T):
      broken = False
      n = int(f.readline())
      counted = {}
      count = 1
      while len(counted) < 10:
        if count > 10000:
          print "Case #{}: INSOMNIA".format(t+1)
          broken = True
          break
        for e in list(str(n*count)):
          if e not in counted:
            counted[e] = 1
        count += 1
      # print counted, len(counted)
      if not broken: print "Case #{}: {}".format(t+1, n*(count-1))

if __name__ == '__main__':
  count_sheep(sys.argv[1])