

def solve(N):
  if N == 0: return 'INSOMNIA'
  has = [False for i in xrange(10)]
  numd = 0
  c = 1
  while True:
    tmp = c*N
    while tmp:
      digit = tmp % 10
      if not has[digit]:
        has[digit] = True
        numd += 1
      tmp = tmp / 10
    if numd == 10: return c*N
    c += 1
    if c == 1000000: return 'INSOMNIA'
    

f = open('A-large.in')
fo = open('output_A_large.out', 'w')

NT = int(f.readline())
for t in xrange(NT):
  N = int(f.readline())
  fo.write('Case #' + str(t+1) + ': ' + str(solve(N)) + '\n')
  

f.close()
fo.close()