import numpy as np

fout = open('output.txt', 'wb')
fout.write('Case #1:\n')

n, j = 16, 50

used = set()

for i in xrange(j):
  while True:
    z = np.random.randint(2, size=(n,))
    z[0] = 1
    z[n - 1] = 1
    z_str = ''.join(map(str, z))[::-1]
    if z_str in used:
      continue
    
    is_prime = False
    divs = []
    for base in range(2, 11):
      num = 0
      cur_pow = 1
      for i in range(n):
        num += z[i] * cur_pow
        cur_pow *= base

      divider = -1
      for i in xrange(2, int(np.sqrt(num)) + 2):
        if num % i == 0:
          divider = i
          break

      if divider == -1:
        is_prime = True
        break

      divs.append(divider)

    if not is_prime:
      used.add(z_str)
      fout.write(z_str)
      print z_str
      fout.write(' ')
      fout.write(' '.join(map(str, divs)))
      fout.write('\n')
      break
