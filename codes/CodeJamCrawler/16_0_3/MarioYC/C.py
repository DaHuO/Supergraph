print "Case #1:"

N = 32
J = 500

def to_base2(n):
  ret = ""
  
  while n > 0:
    if n % 2 == 0:
      ret = "0" + ret
    else:
      ret = "1" + ret
    n /= 2
  
  return ret

for i in range(0,J):
  aux = 2**(N / 2 - 1) + 2 * i + 1
  aux = 2**(N / 2) * aux + aux
  sol = to_base2(aux)
  conv = [0] * 10
  
  for j in range(0,N / 2):
    if sol[j] == '1':
      for k in range(2,11):
        conv[k - 2] += k ** (N / 2 - 1 - j)
  
  for k in range(0,9):
    sol += " " + str(conv[k])
  
  print sol
