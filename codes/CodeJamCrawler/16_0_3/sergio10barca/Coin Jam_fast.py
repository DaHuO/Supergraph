import sys

def es_primo_div(n):
  for i in range(2, 101):
    if n%i == 0:
      return i
  return 0

def precalculate(MAX):
  m = []
  m.append([0]*MAX)
  m.append([0]*MAX)
  for i in range(2, 11):
    sum = 1
    m.append([0]*MAX)
    for j in range(MAX):
      m[i][j] = sum
      sum = sum*i 
#  print(m)
  return m

def cambio_base(n, m):
  sum = [0]*11
  cont = 0
  while True:
    if n%2 == 1:
      for j in range(2, 11):
#        print("j = {0} cont {1} sum {2}".format(j, cont, m[j][cont]))
        sum[j] = sum[j]+m[j][cont]
    cont = cont+1
    n = n // 2
    if n == 0:
      break
  cont = 0
  resp = []
  for i in range(2, 11):
    k = es_primo_div(sum[i])
    if k > 0:
      resp.append(k)
    if len(resp) == 9:
      resp.append(sum[10])
      return resp
  return []

def solve(n, k, m):
  lim = 2**n
  lim_inf = (2**(n-1))+1
  ini = lim_inf//6;
  ini = 6*ini+3
  i = ini
  while k > 0 and i < lim:
    v = cambio_base(i, m)
    if len(v) >= 9:
      print("{0}".format(v[len(v)-1]), end = "")
      for j in range(len(v)-1):
        print(" {0}".format(v[j]), end = "")
      print()
      k = k-1;
    i = i+6
  return

m = precalculate(35);
casos = int(input())
for i in range(casos):
  v = [int(x) for x in input().split()]
  n = v[0]
  j = v[1]
  print("Case #{0}:\n".format(i+1), end = "")
  solve(n, j, m)