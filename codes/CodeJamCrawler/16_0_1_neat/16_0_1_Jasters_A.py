from sys import stdin, argv

def main():
  if len(argv) > 1: infile = open(argv[1], 'rU')
  else: infile = stdin

  for case in xrange(1, int(infile.readline()) + 1):
    N = int(infile.readline().strip())
    if N == 0:
      print "Case #" + str(case) + ": INSOMNIA"
      continue
    else:
      seen = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
      M = N
      while True:
        M_str = str(M)
        for c in M_str:
          seen[int(c)] = 1
        all_seen = True
        for i in xrange(0, 10):
          if seen[i] == 0:
            all_seen = False
            break
        if all_seen:
          break
        M += N
    print "Case #" + str(case) + ": " + str(M)


if __name__ == '__main__':
  main()
