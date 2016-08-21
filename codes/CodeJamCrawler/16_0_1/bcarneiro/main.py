def solve(line):
  digits_seen = {}
  n = int(line)
  for i in range(1, 101):
    for c in str(i*n):
      digits_seen[c] = True

    if len(digits_seen) == 10:
      return i*n
  return 'INSOMNIA'


if __name__ == "__main__":
  n = input()

  for i in xrange(1, n+1):
    line = raw_input()
    print("Case #{0}: {1}".format(i, solve(line)))
