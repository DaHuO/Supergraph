fname = "B-large.in.txt"
# fname = "test.in"

def to_str(l):
  return "".join(l)

def truncate(l):
  while len(l) > 0 and l[len(l)-1] == "+":
    l.pop()
  return l

def first(l):
  i = 0
  while l[i] == "+":
    i += 1
  return i

def flip(l):
  return ["+" if x == "-" else "-" for x in l]

def solve(pans):
  cnt = 0
  pans = truncate(pans)
  if len(pans) == 0:
    return cnt
  f = first(pans)
  if f > 0:
    return 1 + solve(flip(pans[:f]) + pans[f:])
  return 1 + solve(flip(pans[::-1]))


def main():
  with open(fname) as f:
    for i in xrange(int(f.readline())):
      pans = list(f.readline().strip())
      print 'Case #%s: %s' % (i + 1, solve(pans))

main()