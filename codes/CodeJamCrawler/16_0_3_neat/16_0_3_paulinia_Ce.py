t = int(input())

for i in range(0, t):
  print("Case #" + str(i + 1) + ":")
  n, j = map(int, input().split())
  k = n - 2
  a = 0
  while j > 0:
    bits = '1'
    b = a
    while(len(bits) < k + 1):
      if b % 2 == 1:
        bits += '1'
      else:
        bits += '0'
      b = b // 2
    bits += '1'
    bits = bits[::-1]
    divisors = []
    for l in range(2, 11):
      num = int(bits, l)
      p = 2
      bolo = -1
      while p * p <= num:
        if num % p == 0:
          bolo = p
          break
        p += 1
      if bolo != -1:
        divisors.append(p)
      else:
        break
    if len(divisors) < 9:
      a += 1
      continue
    j -= 1
    print(bits, end = " ")
    print(' '.join(map(str, divisors)))
    a += 1
    