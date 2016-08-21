from sys import stdin, argv

def main():
  if len(argv) > 1: infile = open(argv[1], 'rU')
  else: infile = stdin

  for case in xrange(1, int(infile.readline()) + 1):
    S = infile.readline().strip()
    prev = S[0]
    num_moves = 0
    for c in S:
      if c != prev:
        num_moves += 1
      prev = c
    if c != '+':
      num_moves += 1
    print "Case #" + str(case) + ": " + str(num_moves)


if __name__ == '__main__':
  main()
