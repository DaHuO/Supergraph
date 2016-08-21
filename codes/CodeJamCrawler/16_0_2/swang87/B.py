infile = 'B-large.in'
outfile = 'B-large-out.txt'

def flips(pancakes):
  # flip is number of sign changes plus 1 if last one is '-'
  n = 0
  for p in xrange(1, len(pancakes)):
    n += pancakes[p] != pancakes[p-1]
  if pancakes[-1] == '-':
    n += 1
  return n
      
def main():
  out = open(outfile, 'w')
  f = open(infile)
  N = int(f.readline())
  for n in xrange(N):
    i = f.readline().strip()
    out.write("Case #"+str(n+1)+": "+str(flips(i))+"\n")


main()

