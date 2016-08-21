n_cases = int(input())

for case_num in range(1, n_cases+1):
  N = int(input())
  if N == 0:
    print("Case #{}: {}".format(case_num, "INSOMNIA"))
    continue

  Ns = N
  digits = set()
  while len(digits) < 10:
    for digit in str(Ns):
      digits.add(digit)
    Ns += N

  print("Case #{}: {}".format(case_num, Ns-N))
