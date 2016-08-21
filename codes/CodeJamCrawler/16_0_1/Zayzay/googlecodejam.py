import sys

def countingSheep(input):
  with open(input) as f:
    next(f)
    outfile = open('output.txt', 'w')
    T = 1
    for line in f:
      N = int(line)
      if N == 0:
        outfile.write('Case #%d: INSOMNIA\n' % T)
      else:
        digitTracker = set()
        i = 1
        while len(digitTracker) != 10:
          number = N * i
          strNumber = str(number)
          for digit in strNumber:
            digitTracker.add(digit)
          i += 1
        outfile.write('Case #%d: %d\n' % (T, number))
      T += 1

if __name__ == "__main__":
  if len(sys.argv) == 2:
    countingSheep(sys.argv[1])
  else:
    print 'please specify an input file'