### Google CodeJam 2016: Counting Sheep ###

def get_digits(num):
  """Extracts the digits from a number into a set."""
  digits = set()
  for digit in str(num):
    digits.add(int(digit))
  return digits

def solve_case(N):
  """Solves a test case."""
  if N == 0:
    return "INSOMNIA"
  seen_digits = set()
  curr_num = 0
  while len(seen_digits) < 10:
    curr_num += N
    curr_digits = get_digits(curr_num)
    seen_digits |= curr_digits
  return str(curr_num)

for i in range(input()):
  print("Case #%d: %s" % (i + 1, solve_case(input())))

