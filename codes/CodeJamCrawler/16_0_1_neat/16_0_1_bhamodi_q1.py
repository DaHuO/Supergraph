t = int(input())
for i in range(1, t + 1):
  number_set = set()
  num = int(input())
  j = 1
  text_to_show = str(num)
  while True:
    if j > 100:
      text_to_show = 'INSOMNIA'
      break
    new_num = num * j
    for digit in str(new_num):
      number_set.add(digit)
    if len(number_set) == 10:
      text_to_show = str(new_num)
      break
    else:
      j += 1


  print('Case #' + str(i) + ': ' + text_to_show)
