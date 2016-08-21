n = int(input())

for i in range(0, n):
  a = int(input())
  if a == 0:
    print("Case #" + str(i + 1) + ": INSOMNIA")
    continue
  boli = [False] * (58 + 1)
  rem = 10
  n = a
  while rem > 0:
    s = str(n)
    for c in s:
      if boli[int(c)] == False:
        boli[int(c)] = True
        rem -= 1
    n += a
  print("Case #" + str(i + 1) + ": " + str(n - a))
  