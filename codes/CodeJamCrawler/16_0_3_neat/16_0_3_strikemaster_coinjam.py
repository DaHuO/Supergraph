import math

def interpret(base, num):
  reverse = reversed(num)
  final = 0
  for idx,el in enumerate(reverse):
    final += el*(base**idx)
  return final

# Return none if prime
def find_divisor(num):
  i = 2
  while i <= math.sqrt(num):
    if num % i == 0:
      return i
    i += 1
  None


# Output format is list of tuples (jamcoin str, list of divisors)
def coinjam(n, j):
  ans_tuples = []
  # Assume n 2 3
  vary_num = n-2
  for i in range(2**vary_num):
    if len(ans_tuples) == j:
      return ans_tuples
    binary = bin(i)[2:]
    padded = '0' * (vary_num-len(binary)) + binary
    bin_list = [1] + [int(x) for x in list(padded)] + [1]
    # list from 2 to 10
    divisors = []
    for base in range(2,11):
      interpreted = interpret(base, bin_list)
      divisor = find_divisor(interpreted)
      if divisor is None:
        break
      else:
        divisors.append(divisor)
    if len(divisors) == 9:
      bin_str = ''.join([str(x) for x in bin_list])
      print len(ans_tuples), bin_str
      ans_tuples.append((bin_str, divisors))
