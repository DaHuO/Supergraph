import math

def SeriesGenerator(x):
    A = Power+10*int(bin(x)[2:])
    return A

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True

def divisorGenerator(n):
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield int(i)

def Bases(x):
    for _ in range(2, 11):
        yield int(x, _)


T = int(input())
for _ in range(T):
    N, J = map(int, input().split())
    Power = 10**(N-1)+1
    i = 0
    print('Case #{}:'.format(_+1))
    while(J>0):
        D = {}
        X = SeriesGenerator(i)
        L = list(Bases(str(X)))
        counter = 1
        for base in L:
            if is_prime(base)==False:
                counter += 1
                D[counter]=list(divisorGenerator(base))[1]

            if counter==10:
                J -= 1

                print(X, end = ' ')
                for k in range(2,11):
                    print(D[k], end = ' ')
                print('')
        i += 1
