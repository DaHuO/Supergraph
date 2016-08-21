import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-i', '--input', help="input_file")
parser.add_argument('-o', '--output', help="output_file")
args = parser.parse_args()

def solve(data):
  n = int(data[0])
  if n == 0:
    return "INSOMNIA"
  seen = set()
  for i in xrange(1, 1000):
    num = i * n
    for c in str(num):
      seen.add(c)
    if len(seen) == 10:
      return num
  print "Failed at %s" % n
  return "INSOMNIA"

with open(args.input, 'r') as inf, open(args.output, 'w') as outf:
  n = int(inf.next())
  c = 0
  for line in inf:
    c += 1
    ans = solve(line.strip().split())
    print >> outf, "Case #%s: %s" % (c, ans)
    n -= 1

assert n == 0
