import sys, StringIO


def solution(s):
  r = []
  for c in s:
    if len(r)>0 and c>=r[0]:
      r.insert(0, c)
    else:
      r.append(c)
  return "".join(r)
#solution


if __name__ == '__main__':
  if len(sys.argv)>1:
    input = file(sys.argv[1])
  else:
    input = StringIO.StringIO("""7
CAB
JAM
CODE
ABAAB
CABCBBABC
ABCABCABC
ZXCASDQWE """)
  cases = int(input.readline())
  for case in range(cases):
    s = list(input.readline().strip())
    print("Case #%d: %s" % (case+1, solution(s)))
