import math

SOL = []
A = []
N = 0
J = 0
FINISH = False

table = [[1 for pos in xrange(32)] for base in xrange(11)]
for base in range(2, 11):
  for pos in range(1, 32):
    table[base][pos] = base * table[base][pos - 1]


def is_prime(val):
  for i in range(2, int(math.sqrt(val))):
    if val % i == 0: return i
  return True

def check():
  global A, N, J, SOL, FINISH
  
  divisors = []
  for base in range(2, 11):
    val = 0
    for pos in range(N):
      if A[pos] == 1: val += table[base][pos]
    
    p = is_prime(val)
    if p == True: return
    divisors.append(p)
  
  SOL.append(''.join([str(x) for x in A[::-1]]) + ' ' + ' '.join([str(x) for x in divisors]))
  if len(SOL) == J: FINISH = True
  #print len(SOL)
  

def rek(k):
  global N, A
  if FINISH: return
  if k == N - 1: check()
  else:
    A[k] = 0
    rek(k+1)
    A[k] = 1
    rek(k+1)

def solve():
  global N, J, A
  A = [1 for i in xrange(N)]
  rek(1)

###################################################################################################

f = open('input_C.txt')
fo = open('output_C.txt', 'w')

NT = int(f.readline())
for t in xrange(NT):
  S = f.readline().strip()
  S = S.split()
  N = int(S[0])
  J = int(S[1])
  solve()
  fo.write('Case #' + str(t+1) + ':\n')
  for s in SOL: fo.write(s + '\n')
  

f.close()
fo.close()