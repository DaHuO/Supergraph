import sys, StringIO


#this will flip all pancakes until the last pancape is 0 and the current is 1.
def flip(pancake):
  i = 1
  while i<len(pancake) and not(pancake[i-1] == 0 and pancake[i] == 1):
    i+=1
  j=0
  while j<i:
    pancake[j] = (pancake[j]+1)%2
    j+=1
  return pancake

def solve(pancake):
  c = 0
  while sum(pancake)<len(pancake):
    pancake = flip(pancake)
    c+=1
  return c

def solve2(pancake):
  c = 0
  for i in range(1,len(pancake)):
    c += pancake[i-1]!=pancake[i]
  return c


if __name__ == '__main__':
  if len(sys.argv)>1:
    input = file(sys.argv[1])
  else:
    input = StringIO.StringIO("""5
-
-+
+-
+++
--+-""")
  cases = int(input.readline())
  for case in range(cases):
    p = [x=='+' and 1 or 0 for x in input.readline().strip()]
    print("Case #%d: %s" % (case+1, solve(p)))
