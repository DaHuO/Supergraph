t = int(raw_input())
for tc in range(1, t + 1):
  n = int(raw_input())
  if n == 0:
    print("Case #%d: INSOMNIA"%(tc))
    continue
  count = 0
  seen_digits = set()
  while len(seen_digits) < 10:
    count += 1
    number = n * count
    for digit in str(number):
      seen_digits.add(digit)
  print("Case #%d: %d"%(tc, number))
