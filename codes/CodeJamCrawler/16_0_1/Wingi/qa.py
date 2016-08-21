import sys, StringIO

def solution(n):
  d = set()
  i=1
  s=n
  if n==2*n:
    return "INSOMNIA"

  while i<10000:
    d.update(list(str(s)))
    #print d
    if len(d)==10:
      return s
    i+=1
    s+=n
  return "INSOMNIA"

if __name__ == '__main__':
  if len(sys.argv)>1:
    input = file(sys.argv[1])
  else:
    input = StringIO.StringIO("""5
0
1
2
11
1692""")
  cases = int(input.readline())
  for case in range(cases):
    n = int(input.readline())
    print("Case #%d: %s" % (case+1, solution(n)))
