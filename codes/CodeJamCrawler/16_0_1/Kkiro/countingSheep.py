def checkDigits(digits):
  return sum(digits) == 10

T = int(input())
for p in range(0, T):
  N = int(input())
  digits = []
  for i in range(0, 10):
    digits.insert(i, 0)
  repeat = 0
  while repeat < 100000:
    repeat += 1
    num = N * repeat
    while num > 0:
      digits[num%10] = 1
      num //= 10
    if checkDigits(digits):
      break
  if checkDigits(digits):
    print('Case #' + str(p+1) + ': '+ str(N * repeat))
  else:
    print('Case #' + str(p+1) + ': '+ 'INSOMNIA')
