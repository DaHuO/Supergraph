file = "large.in"

def counting_sheep(N):
  if not N:
    return 'INSOMNIA'

  digits = set(range(10))
  y = 0

  while digits:
    y += 1
    num = y * N
    digits -= set(map(int, str(num)))

  return num

with open(file) as handle:
  T = int(handle.readline())

  for x in range(T):
    N = int(handle.readline())

    print "Case #{}: {}".format(x + 1, counting_sheep(N))
