infile = 'A-large.in'
outfile = 'A-large-out.txt'

def need(n):
  digits = set()
  if n == 0:
    return 'INSOMNIA'
  for i in xrange(1000000):
    digits.update(set(str(n*(i+1))))
    if len(digits) == 10:
      return str(n*(i+1))
  return 'INSOMNIA'

      
def main():
  out = open(outfile, 'w')
  f = open(infile)
  N = int(f.readline())
  for n in xrange(N):
    i = int(f.readline())
    out.write("Case #"+str(n+1)+": "+need(i)+"\n")


main()

