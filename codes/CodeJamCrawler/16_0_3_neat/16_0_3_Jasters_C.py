from sys import stdin, argv

MAX_DIVISOR = 100

def main():
  if len(argv) > 1: infile = open(argv[1], 'rU')
  else: infile = stdin

  for case in xrange(1, int(infile.readline()) + 1):
    print 'Case #' + str(case) + ':'
    N, J =  infile.readline().split()
    N = int(N)
    J = int(J)
    jam_str = "1"
    n = N - 2
    count = 0
    for i in xrange(0, 2**n):
      if count == J:
        break
      b = bin(i)[2:]
      jam_str = "1" + str(0) * (n - len(b)) + b + "1"
      divisors = [0, 0, 0, 0, 0, 0, 0, 0, 0]
      is_prime = False
      for base in xrange(2, 11):
        divisors[base-2] = get_divisor(str_to_base_n(jam_str, base))
        if divisors[base-2] == 0:
          is_prime = True
          break
      if not is_prime:
        divisors_str = ""
        for divisor in divisors:
          divisors_str += str(divisor) + " "
        print jam_str, divisors_str
        count += 1


def get_divisor(n):
  if n == 2:
    return True
  if n % 2 == 0:
    return 2
  root = int(n**.5)
  max_divisor = min(root, MAX_DIVISOR)
  divisor = 3
  while(divisor <= max_divisor):
    if n % divisor == 0:
      return divisor
    divisor += 2
  return 0


def str_to_base_n(num_str, n):
  m = 1
  val = 0
  for c in num_str[::-1]:
    if c == '1':
      val += m
    m *= n
  return val


if __name__ == '__main__':
  main()
