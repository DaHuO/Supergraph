print "Case #1:"

powers = [[i ** j for j in range(32)] for i in range(11)]

count = 0

for c in range((1<<31) + 1, 1 << 32, 2):

  divisors = [0] * 9
  X = c
  numbers = [0] * 9
  numstr = ""
  for i in range(32):
    for j in range(9):
      numbers[j] += powers[j+2][i] * (X % 2)
    numstr = str(X % 2) + numstr
    X /= 2
  for i in range(3, 1<<16 + 1, 2):
    for j in range(9):
      if numbers[j] % i == 0:
        divisors[j] = i
  if 0 not in divisors:
    print numstr, " ".join([str(x) for x in divisors])
    count += 1
    if count == 500:
      break

