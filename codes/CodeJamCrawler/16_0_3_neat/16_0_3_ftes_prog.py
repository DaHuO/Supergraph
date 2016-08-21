import math

def find(n, j):
  # n length, j coins
  for x_str in bit_strings(n):
    if j == 0: return
    divisors = check(x_str)
    if divisors:
      print('%s %s' % (x_str, ' '.join(divisors)))
      j -= 1
  print('missing %i coins' % j)

def check(x_str):
  divisors = []
  for i in range(2, 11):
    n_in_base = base_to_dec(x_str, i)
    divisor = get_divisor(n_in_base)
    if not divisor:
      return False
    divisors.append(str(divisor))
  return divisors

def base_to_dec(x_str, b):
  n = 0
  factor = 1
  for i in reversed(x_str):
    n += factor * int(i)
    factor *= b
  return n

def bit_strings(length):
  for i in range(int(math.pow(2, length-2))):
    yield '1' + format(i, 'b').rjust(length-2, '0') + '1'

def get_divisor(n):
    if n % 2 == 0 and n > 2:
      return 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
      if n % i == 0: return i
    return False


if __name__ == '__main__':
  # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
  # This is all you need for most Google Code Jam problems.
  t = int(input())  # read a line with a single integer
  for i in range(1, t + 1):
    n, j = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    print('Case #1:')
    find(n, j)
