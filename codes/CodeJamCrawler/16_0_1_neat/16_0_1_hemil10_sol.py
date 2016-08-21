t = int(input())
inp = []
for i in range(t):
  inp.append(int(input()))


for i in range(t):
  n = inp[i]
  if n == 0:
    print("Case #%d: INSOMNIA" %(i + 1))
    continue

  temp = n
  count = [0 for x in range(0,10)]
  s = 0
  ct = 1
  while s != 10:

    while n > 0:
      d = n % 10
      if count[d] == 0:
        count[d] += 1
        s += 1
      n = n/10

    if s == 10:
      print("Case #%d: %d" %(i + 1, temp*ct))
    ct += 1
    n = temp * ct
