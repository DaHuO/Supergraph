t = int(input())

for i in range(0, t):
  pancakes = input()
  last = ' '
  kusy = 0
  for c in pancakes:
    if c != last:
      last = c
      kusy += 1
  
  if last == '+':
    kusy -= 1
  print("Case #" + str(i + 1) + ": " + str(kusy))