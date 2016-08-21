import numpy as np


def compute(N):
  seen = np.zeros(10)
  if N == 0:
    return 'INSOMNIA'
  i = 1
  n = N

  while (True):
    n_str = str(n)
    for c in n_str:
      seen[int(c)] = 1

    if all(seen):
      return n
    i += 1
    n = N * i




with open('A-large.in.txt', 'rb') as input_file:
  next(input_file)
  i = 1
  with open('output.txt', 'wb') as output_file:
    for line in input_file:
      output_file.write('Case #{}: {}\n'.format(i, compute(int(line))))
      i += 1